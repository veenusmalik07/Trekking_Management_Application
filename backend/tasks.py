import csv
import os
from datetime import date, timedelta
from html import escape

from celery import shared_task
from flask_mail import Message
from models import db, Booking, Notification, Trek, User
from mails import send_email

from extensions import mail

@shared_task(ignore_result=True)
def send_email_task(receiver, subject, body):
    send_email(receiver, subject, body)


@shared_task(ignore_result=True)
def daily_reminder():
    """Email confirmed customers one day before their trek begins."""
    reminder_date = date.today() + timedelta(days=1)
    bookings = (
        Booking.query.join(Trek)
        .filter(
            Booking.booking_status == "Accepted",
            Trek.start_date == reminder_date,
        )
        .all()
    )

    for booking in bookings:
        trek = booking.trek
        instructions = trek.equipment_required or "Please follow the instructions shared by your trek leader."
        subject = f"Reminder: {trek.trek_name} starts tomorrow"
        body = f"""Hello {booking.user.full_name},

This is a reminder that your trek, {trek.trek_name}, starts on {trek.start_date.strftime('%d %B %Y')}.
Meeting point: {trek.meeting_point}
Location: {trek.location}
Instructions: {instructions}

Please arrive on time and carry the required equipment. Have a safe trek!

TrekMate Team"""
        send_email_task.delay(booking.user.email, subject, body)

    print(f"Daily trek reminder queued for {len(bookings)} booking(s).")

@shared_task(ignore_result=True)
def monthly_report():
    """Send every admin an HTML report covering the preceding calendar month."""
    today = date.today()
    previous_month_last_day = today.replace(day=1) - timedelta(days=1)
    month_start = previous_month_last_day.replace(day=1)
    month_end = previous_month_last_day
    report_month = month_start.strftime("%B %Y")

    completed_treks = Trek.query.filter(
        Trek.end_date.between(month_start, month_end)
    ).count()
    accepted_bookings = Booking.query.join(Trek).filter(
        Booking.booking_status == "Accepted",
        Trek.end_date.between(month_start, month_end),
    )
    unique_users = accepted_bookings.with_entities(Booking.user_id).distinct().count()
    participant_places = db.session.query(
        db.func.coalesce(db.func.sum(Booking.number_of_people), 0)
    ).select_from(Booking).join(Trek).filter(
        Booking.booking_status == "Accepted",
        Trek.end_date.between(month_start, month_end),
    ).scalar()
    popular_treks = (
        db.session.query(
            Trek.trek_name,
            db.func.sum(Booking.number_of_people).label("participants"),
        )
        .join(Booking)
        .filter(
            Booking.booking_status == "Accepted",
            Trek.end_date.between(month_start, month_end),
        )
        .group_by(Trek.id, Trek.trek_name)
        .order_by(db.desc("participants"), Trek.trek_name)
        .limit(5)
        .all()
    )
    popular_rows = "".join(
        f"<li>{escape(trek_name)} — {participants} participant(s)</li>"
        for trek_name, participants in popular_treks
    ) or "<li>No completed treks recorded.</li>"

    html = f"""
    <h2>TrekMate monthly activity report — {report_month}</h2>
    <p>Reporting period: {month_start.strftime('%d %b %Y')} to {month_end.strftime('%d %b %Y')}</p>
    <ul>
      <li><strong>Treks conducted:</strong> {completed_treks}</li>
      <li><strong>Unique users participated:</strong> {unique_users}</li>
      <li><strong>Total participant places:</strong> {participant_places}</li>
    </ul>
    <h3>Popular treks</h3>
    <ol>{popular_rows}</ol>
    """

    admins = User.query.filter_by(role="admin", status="Active").all()
    for admin in admins:
        msg = Message(
            subject=f"TrekMate Monthly Activity Report — {report_month}",
            recipients=[admin.email],
            html=html,
        )
        mail.send(msg)

    print(f"Monthly report sent to {len(admins)} active admin(s).")

@shared_task
def export_booking_csv(user_id):
    """Generate a user's booking-history CSV and notify them when it is ready."""
    user = db.session.get(User, user_id)
    if not user:
        raise ValueError("User not found.")

    bookings = Booking.query.filter_by(user_id=user_id).order_by(
        Booking.booking_date.desc()
    ).all()
    filename = f"booking_history_{user_id}.csv"
    export_directory = os.path.join(os.getcwd(), "exports")
    filepath = os.path.join(export_directory, filename)
    os.makedirs(export_directory, exist_ok=True)

    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "User ID",
            "Trek Name",
            "Location",
            "Booking Status",
            "Booking Date",
            "Trek Start Date",
            "Trek End Date",
        ])
        for booking in bookings:
            writer.writerow([
                user.id,
                booking.trek.trek_name,
                booking.trek.location,
                booking.booking_status,
                booking.booking_date.strftime("%d %b %Y"),
                booking.trek.start_date.strftime("%d %b %Y"),
                booking.trek.end_date.strftime("%d %b %Y"),
            ])

    try:
        msg = Message("Your TrekMate booking history", recipients=[user.email])
        msg.body = "Your requested booking-history CSV is attached to this email."
        with open(filepath, "rb") as file:
            msg.attach(filename, "text/csv", file.read())
        mail.send(msg)
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)

    notification = Notification(
        receiver_id=user.id,
        title="Booking history ready",
        message="Your booking-history CSV has been sent to your email address.",
        notification_type="Export",
        priority="Normal",
    )
    db.session.add(notification)
    db.session.commit()

    return {"message": "Booking-history CSV sent by email."}
