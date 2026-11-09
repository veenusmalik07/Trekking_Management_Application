# IMPORT REQUIRED LIBRARIES
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import func
from models import Notification
from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
import json
import os
from flask import current_app
from sqlalchemy import extract
from collections import OrderedDict
from extensions import cache


# IMPORT DATABASE MODELS
from models import (
    db,
    User,
    StaffProfile,
    Trek,
    Booking,
    TrekMedia,
    StaffAssignment
)

# CREATE API BLUEPRINT
api_bp = Blueprint(
    "api",
    __name__
)

# ADMIN DASHBOARD
@api_bp.route("/api/admin/dashboard", methods=["GET"])
def admin_dashboard():

    # SUMMARY
    total_users = User.query.filter_by(role="user").count()
    total_staff = StaffProfile.query.count()
    total_treks = Trek.query.count()
    total_bookings = Booking.query.count()

    # RECENT BOOKINGS
    recent_bookings = []
    bookings = Booking.query.order_by(Booking.booking_date.desc()).limit(5).all()
    for booking in bookings:
        recent_bookings.append({
            "id": booking.id,
            "booking_reference": booking.booking_reference,
            "user_name": booking.user.full_name,
            "trek_name": booking.trek.trek_name,
            "booking_status": booking.booking_status
        })

    # UPCOMING TREKS
    upcoming_treks = []
    treks = Trek.query.filter_by(status="Upcoming").order_by(Trek.start_date.asc()).limit(5).all()
    for trek in treks:
        upcoming_treks.append({
            "id": trek.id,
            "trek_name": trek.trek_name,
            "start_date": trek.start_date.strftime("%d %b %Y"),
            "available_slots": trek.available_slots,
            "capacity": trek.capacity,
            "status": trek.status
        })

    # BOOKING STATUS
    pending_count = Booking.query.filter_by(booking_status="Pending").count()
    accepted_count = Booking.query.filter_by(booking_status="Accepted").count()
    rejected_count = Booking.query.filter_by(booking_status="Rejected").count()

    # TREK STATUS
    available_count = Trek.query.filter_by(status="Available").count()
    upcoming_count = Trek.query.filter_by(status="Upcoming").count()
    ongoing_count = Trek.query.filter_by(status="Ongoing").count()
    completed_count = Trek.query.filter_by(status="Completed").count()
    cancelled_count = Trek.query.filter_by(status="Cancelled").count()

    # total revenue
    total_revenue = db.session.query(db.func.sum(Booking.total_amount)).filter(Booking.booking_status == "Accepted").scalar() or 0

    # monthly revenue
    from datetime import datetime
    current_month = datetime.utcnow().month
    current_year = datetime.utcnow().year
    monthly_revenue = db.session.query(
    db.func.sum(Booking.total_amount)).filter(
        Booking.booking_status == "Accepted",
        db.extract("month", Booking.booking_date) == current_month,
        db.extract("year", Booking.booking_date) == current_year
        ).scalar() or 0

    # RESPONSE
    return jsonify({
        "success": True,
        "data": {
            "summary":{
                "total_users": total_users,
                "total_staff": total_staff,
                "total_bookings": total_bookings,
                "total_revenue": total_revenue,
                "monthly_revenue": monthly_revenue
            },
            "recent_bookings": recent_bookings,
            "upcoming_treks": upcoming_treks,
            "booking_chart": {
                "Accepted": accepted_count,
                "Pending": pending_count,
                "Rejected": rejected_count
            },
            "trek_chart": {
                "Available": available_count,
                "Upcoming": upcoming_count,
                "Ongoing": ongoing_count,
                "Completed": completed_count,
                "Cancelled": cancelled_count
            }
        }
    }), 200

# ADMIN TREKS START
# ADMIN TREKS DASHBOARD
@api_bp.route("/api/admin/treks", methods=["GET"])
def get_all_treks():
    treks = Trek.query.all()
    trek_list = []
    for trek in treks:
        trek_list.append({
            "id": trek.id,
            "trek_name": trek.trek_name,
            "trek_type": trek.trek_type,
            "location": trek.location,
            "meeting_point": trek.meeting_point,
            "state": trek.state,
            "difficulty": trek.difficulty,
            "emergency_level": trek.emergency_level,
            "duration": trek.duration,
            "price": trek.price,
            "capacity": trek.capacity,
            "available_slots": trek.available_slots,
            "minimum_age": trek.minimum_age,
            "maximum_age": trek.maximum_age,
            "fitness_requirement": trek.fitness_requirement,
            "equipment_required": trek.equipment_required,
            "description": trek.description,
            "cover_image": trek.cover_image,
            "start_date": trek.start_date,
            "end_date": trek.end_date,
            "status": trek.status,
            "booking_count": len(trek.bookings)
        })
    return jsonify({
        "success": True,
        "data": trek_list
    })


# CREATE NEW TREK
@api_bp.route("/api/admin/create-trek", methods=["POST"])
def create_trek():
    # Get JSON data sent from Vue
    data = request.get_json()
    today = datetime.utcnow().date()
    start_date = datetime.strptime(data["start_date"], "%Y-%m-%d").date()
    end_date = datetime.strptime(data["end_date"], "%Y-%m-%d").date()

    if start_date < today:
        return jsonify({
        "success": False,
        "message": "Start date cannot be in the past."
    }),400
    if end_date < start_date:
        return jsonify({
        "success": False,
        "message": "End date must be after start date."
    }),400


    registration_deadline = datetime.strptime(data["registration_deadline"], "%Y-%m-%d").date()
    if registration_deadline >= start_date:
        return jsonify({
        "success":False,
        "message":"Registration deadline must be before trek start date."
    }),400

    if int(data["available_slots"]) > int(data["capacity"]):
        return jsonify({
        "success": False,
        "message": "Available slots cannot exceed total capacity."
    }), 400

    # Create Trek Object
    trek = Trek(
        trek_name=data["trek_name"],
        trek_type=data["trek_type"],
        location=data["location"],
        meeting_point=data["meeting_point"],
        state=data["state"],
        difficulty=data["difficulty"],
        emergency_level=data["emergency_level"],
        duration=int(data["duration"]),
        price=float(data["price"]),
        description=data["description"],
        organizer=data["organizer"],
        capacity=int(data["capacity"]),
        available_slots=int(data["available_slots"]),
        cover_image=data.get("cover_image"),
        minimum_age=int(data["minimum_age"]) if data.get("minimum_age") else None,
        maximum_age=int(data["maximum_age"]) if data.get("maximum_age") else None,
        fitness_requirement=data.get("fitness_requirement"),
        equipment_required=data.get("equipment_required"),
        start_date=start_date,
        end_date=end_date,
        registration_deadline=registration_deadline,
        status=data.get("status", "Upcoming")
    )

    # Save Trek
    db.session.add(trek)
    db.session.commit()

    gallery = data.get("gallery_images", "").split("\n")

    for url in gallery:
        url = url.strip()
        if url:
            media = TrekMedia(
                trek_id=trek.id,
                media_type="image",
                media_url=url,
                caption=""
            )
            db.session.add(media)
        db.session.commit()
        cache.delete("user-browse-treks")

    # Success Response
    return jsonify({
        "success": True,
        "message": "Trek created successfully.",
        "trek_id": trek.id
    }), 201


# GET SINGLE TREK DETAILS FOR ADMIN
@api_bp.route("/api/admin/treks/<int:trek_id>", methods=["GET"])
def get_single_trek(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    # GALLERY
    gallery = []

    for media in trek.media:

        gallery.append({

            "id": media.id,

            "media_type": media.media_type,

            "media_url": media.media_url,

            "caption": media.caption

        })

    # ======================================================
    # ASSIGNED STAFF
    # ======================================================

    staff_list = []

    for assignment in trek.staff_assignments:

        user = assignment.staff

        profile = user.staff_profile

        staff_list.append({

            "id": user.id,

            "name": user.full_name,

            "email": user.email,

            "mobile": user.mobile_number,

            "profession": profile.profession if profile else "",

            "specialization": profile.specialization if profile else "",

            "experience": profile.experience_years if profile else "",

            "role_in_trek": assignment.role_in_trek,

            "assignment_status": assignment.assignment_status

        })

    # ======================================================
    # RECENT BOOKINGS
    # ======================================================

    recent_bookings = []

    revenue = 0

    bookings = Booking.query.filter_by(

        trek_id=trek.id

    ).order_by(

        Booking.booking_date.desc()

    ).limit(5).all()

    for booking in bookings:

        revenue += booking.total_amount

        recent_bookings.append({

            "booking_reference": booking.booking_reference,

            "user_name": booking.user.full_name,

            "people": booking.number_of_people,

            "amount": booking.total_amount,

            "payment_status": booking.payment_status,

            "booking_status": booking.booking_status,

            "booking_date": booking.booking_date.strftime("%d %b %Y")

        })

    # ======================================================
    # SUMMARY
    # ======================================================

    summary = {

        "total_bookings": len(trek.bookings),

        "revenue": revenue,

        "remaining_slots": trek.available_slots,

        "booked_slots": trek.capacity - trek.available_slots

    }

    # ======================================================
    # TREK DATA
    # ======================================================

    trek_data = {
        "id": trek.id,
        "trek_name": trek.trek_name,
        "trek_type": trek.trek_type,
        "location": trek.location,
        "meeting_point": trek.meeting_point,
        "state": trek.state,
        "difficulty": trek.difficulty,
        "emergency_level": trek.emergency_level,
        "duration": trek.duration,
        "price": trek.price,
        "description": trek.description,
        "organizer": trek.organizer,
        "capacity": trek.capacity,
        "available_slots": trek.available_slots,
        "cover_image": trek.cover_image,
        "minimum_age": trek.minimum_age,
        "maximum_age": trek.maximum_age,
        "fitness_requirement": trek.fitness_requirement,
        "equipment_required": trek.equipment_required,
        "start_date": trek.start_date,
        "end_date": trek.end_date,
        "registration_deadline": trek.registration_deadline,
        "status": trek.status,
        "created_at": trek.created_at
    }

    # ======================================================
    # RESPONSE
    # ======================================================

    return jsonify({
        "success": True,
        "message": "Trek fetched successfully.",
        "data": {
            "trek": trek_data,
            "gallery": gallery,
            "staff": staff_list,
            "recent_bookings": recent_bookings,
            "summary": summary
        }
    })


# CHANGES STATUS OF TREK
@api_bp.route("/api/admin/trek/<int:trek_id>/status", methods=["PUT"])
def update_trek_status(trek_id):

    data = request.get_json()

    trek = Trek.query.get(trek_id)

    if not trek:
        return jsonify({
            "message": "Trek not found."
        }),404

    trek.status = data["status"]

    db.session.commit()

    return jsonify({
        "success": True,
        "message": f"Trek {data['status']} successfully."
    }),200

# EDITING TREKS : ADMIN
@api_bp.route("/api/admin/treks/<int:trek_id>", methods=["PUT"])
def update_trek(trek_id):

    try:
        trek = Trek.query.get_or_404(trek_id)
        data = request.get_json()
        today = datetime.utcnow().date()
        start_date = datetime.strptime(data["start_date"], "%Y-%m-%d").date()
        end_date = datetime.strptime(data["end_date"], "%Y-%m-%d").date()
        
        if start_date < today:
            return jsonify({
                "success": False,
                "message": "Start date cannot be in the past."
            }),400

        if end_date < start_date:
            return jsonify({
                "success": False,
                "message": "End date must be after start date."
            }),400

        registration_deadline = datetime.strptime(data["registration_deadline"], "%Y-%m-%d").date()
        if registration_deadline >= start_date:
            return jsonify({
                "success":False,
                "message":"Registration deadline must be before trek start date."
            }),400
        
        if data["available_slots"] > data["capacity"]:
            return jsonify({
                "success": False,
                "message": "Available slots cannot exceed total capacity."
            }), 400

        trek.trek_name = data["trek_name"]
        trek.trek_type = data["trek_type"]
        trek.location = data["location"]
        trek.meeting_point = data["meeting_point"]
        trek.state = data["state"]
        trek.difficulty = data["difficulty"]
        trek.emergency_level = data["emergency_level"]
        trek.duration = data["duration"]
        trek.price = data["price"]
        trek.organizer = data["organizer"]
        trek.capacity = data["capacity"]
        trek.available_slots = data["available_slots"]
        trek.minimum_age = data["minimum_age"]
        trek.maximum_age = data["maximum_age"]
        trek.fitness_requirement = data["fitness_requirement"]
        trek.start_date = start_date
        trek.end_date = end_date
        trek.status = data["status"]
        trek.cover_image = data["cover_image"]
        trek.equipment_required = data["equipment_required"]
        trek.description = data["description"]

        db.session.commit()
        cache.delete("user-browse-treks")

        return jsonify({
            "success": True,
            "message": "Trek updated successfully."
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@api_bp.route("/api/admin/delete-trek/<int:trek_id>", methods=["DELETE"])
@jwt_required()
def delete_trek(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    booking_exists = Booking.query.filter_by(trek_id=trek_id).first()

    if booking_exists:

        return jsonify({

            "success": False,

            "message": "Cannot delete this trek because bookings already exist."

        }), 400

    db.session.delete(trek)

    db.session.commit()

    cache.delete("user-browse-treks")

    return jsonify({

        "success": True,

        "message": "Trek deleted successfully."

    })
# ADMIN TREKS ENDS

# ADMIN USERS START
# admin view user
@api_bp.route("/api/admin/user/<int:user_id>", methods=["GET"])
def admin_view_user(user_id):

    user = User.query.get(user_id)

    if not user:

        return jsonify({

            "success": False,

            "message": "User not found."

        }),404


    bookings = Booking.query.filter_by(
        user_id=user.id
    ).order_by(
        Booking.booking_date.desc()
    ).all()


    total_bookings = len(bookings)

    upcoming_treks = 0

    completed_treks = 0

    cancelled_bookings = 0

    total_spent = 0


    booking_list = []


    for booking in bookings:

        if booking.booking_status == "Upcoming":

            upcoming_treks += 1

        elif booking.booking_status == "Completed":

            completed_treks += 1

        elif booking.booking_status == "Cancelled":

            cancelled_bookings += 1


        total_spent += booking.total_amount


        booking_list.append({

            "id": booking.id,

            "booking_reference": booking.booking_reference,

            "trek_name": booking.trek.trek_name,

            "booking_date": booking.booking_date.strftime("%d %b %Y"),

            "booking_status": booking.booking_status,

            "payment_status": booking.payment_status,

            "amount": booking.total_amount

        })


    return jsonify({

        "success": True,

        "data":{

            "user":{

                "id": user.id,

                "full_name": user.full_name,

                "email": user.email,

                "mobile_number": user.mobile_number,

                "gender": user.gender,

                "date_of_birth": user.date_of_birth.strftime("%d %b %Y"),

                "city": user.city,

                "state": user.state,

                "status": user.status,

                "created_at": user.created_at.strftime("%d %b %Y"),

                "last_login":

                    user.last_login.strftime("%d %b %Y")

                    if user.last_login else "-",

                "profile_picture": user.profile_picture,

                "emergency_contact_name":

                    user.emergency_contact_name,

                "emergency_contact_number":

                    user.emergency_contact_number

            },

            "summary":{

                "total_bookings": total_bookings,

                "upcoming_treks": upcoming_treks,

                "completed_treks": completed_treks,

                "cancelled_bookings": cancelled_bookings,

                "total_spent": total_spent

            },

            "bookings": booking_list

        }

    })

# blocking users: admin
@api_bp.route("/api/admin/users/<int:user_id>/status", methods=["PUT"])
def update_user_status(user_id):

    user = User.query.get_or_404(user_id)

    data = request.get_json()

    user.status = data["status"]

    db.session.commit()

    return jsonify({
        "success": True,
        "message": f"User {user.status.lower()} successfully.",
        "status": user.status
    })
# ADMIN USERS ENDS


# ADMIN BOOKINGS START

# GET ALL BOOKINGS
@api_bp.route("/api/admin/bookings", methods=["GET"])
def get_all_bookings():
    bookings = Booking.query.order_by(Booking.booking_date.desc()).all()
    booking_list = []
    for booking in bookings:
        booking_list.append({
            "id": booking.id,
            "booking_reference": booking.booking_reference,
            "user_name": booking.user.full_name,
            "trek_name": booking.trek.trek_name,
            "number_of_people": booking.number_of_people,
            "total_amount": booking.total_amount,
            "payment_status": booking.payment_status,
            "booking_status": booking.booking_status,
            "booking_date": booking.booking_date.strftime("%d %b %Y")
        })

    return jsonify({
    "success": True,
    "count": len(booking_list),
    "summary":{
        "total": len(booking_list),
        "pending": sum(1 for b in bookings if b.booking_status == "Pending"),
        "accepted": sum(1 for b in bookings if b.booking_status == "Accepted"),
        "rejected": sum(1 for b in bookings if b.booking_status == "Rejected")
    },
    "data": booking_list
})


# GET SINGLE BOOKING
@api_bp.route("/api/admin/bookings/<int:booking_id>", methods=["GET"])
def get_booking(booking_id):

    booking = Booking.query.get(booking_id)

    if not booking:

        return jsonify({

            "success": False,

            "message": "Booking not found."

        }),404

    return jsonify({

        "success": True,

        "data":{

            "booking":{

                "id": booking.id,

                "booking_reference": booking.booking_reference,

                "booking_date": booking.booking_date.strftime("%d %b %Y"),

                "number_of_people": booking.number_of_people,

                "total_amount": booking.total_amount,

                "payment_status": booking.payment_status,

                "booking_status": booking.booking_status,

                "special_requests": booking.special_requests,

                "participant_details": booking.participant_details

            },

            "user":{

                "full_name": booking.user.full_name,

                "email": booking.user.email,

                "mobile_number": booking.user.mobile_number,

                "city": booking.user.city,

                "state": booking.user.state

            },

            "trek":{

                "trek_name": booking.trek.trek_name,

                "location": booking.trek.location,

                "difficulty": booking.trek.difficulty,

                "start_date": booking.trek.start_date.strftime("%d %b %Y"),

                "end_date": booking.trek.end_date.strftime("%d %b %Y")

            }

        }

    })

@api_bp.route("/api/admin/booking/<int:booking_id>", methods=["GET"])
def admin_view_booking(booking_id):

    booking = Booking.query.get(booking_id)

    if not booking:
        return jsonify({
            "success": False,
            "message": "Booking not found."
        }), 404

    user = User.query.get(booking.user_id)
    trek = Trek.query.get(booking.trek_id)

    if not user or not trek:
        return jsonify({
            "success": False,
            "message": "Related data not found."
        }), 404

    # Assigned Staff
    assignment = StaffAssignment.query.filter_by(
        trek_id=trek.id,
        assignment_status="Assigned"
    ).first()

    staff_name = "Not Assigned"

    if assignment:
        staff = User.query.get(assignment.staff_id)
        if staff:
            staff_name = staff.full_name

    # Participant Details
    participants = []

    if booking.participant_details:
        participants = json.loads(booking.participant_details)

    return jsonify({

        "success": True,

        "data": {

            "booking": {

                "id": booking.id,

                "booking_reference": booking.booking_reference,

                "booking_date": booking.booking_date.strftime("%d %b %Y"),

                "booking_status": booking.booking_status,

                "payment_status": booking.payment_status,

                "number_of_people": booking.number_of_people,

                "total_amount": booking.total_amount,

                "special_requests": booking.special_requests

            },

            "user": {

                "id": user.id,

                "full_name": user.full_name,

                "email": user.email,

                "mobile_number": user.mobile_number,

                "city": user.city,

                "state": user.state,

                "emergency_contact_name": user.emergency_contact_name,

                "emergency_contact_number": user.emergency_contact_number

            },

            "trek": {

                "id": trek.id,

                "trek_name": trek.trek_name,

                "location": trek.location,

                "state": trek.state,

                "difficulty": trek.difficulty,

                "start_date": trek.start_date.strftime("%d %b %Y"),

                "end_date": trek.end_date.strftime("%d %b %Y"),

                "cover_image": trek.cover_image,

                "staff_name": staff_name

            },

            "participants": participants

        }

    }), 200


# APPROVE BOOKING 
@api_bp.route("/api/admin/approve-booking/<int:booking_id>", methods=["PUT"])
@jwt_required()
def approve_booking(booking_id):
    admin_id = int(get_jwt_identity())
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({
            "success": False,
            "message": "Booking not found."
        }), 404

    # Booking Already Accepted
    if booking.booking_status == "Accepted":
        return jsonify({
            "success": False,
            "message": "Booking has already been approved."
        }), 400

    # Cancelled Booking
    if booking.booking_status == "Rejected":
        return jsonify({
            "success": False,
            "message": "Cancelled bookings cannot be approved."
        }), 400

    # Payment Check
    if booking.payment_status != "Paid":
        return jsonify({
            "success": False,
            "message": "Payment is still pending."
        }), 400

    data = request.get_json()
    booking.booking_status = "Accepted"
    booking.approved_at = datetime.utcnow()
    booking.approved_by = admin_id
    booking.admin_remarks = data.get(
        "admin_remarks",
        "Booking Approved"
    )

    create_notification(

    receiver_id=booking.user_id,

    title="Booking Confirmed",

    message="Your booking has been confirmed by the administrator.",

    notification_type="Booking",

    related_booking_id=booking.id,

    related_trek_id=booking.trek_id

)

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Booking confirmed successfully."
    }), 200

# REJECT BOOKING
@api_bp.route("/api/admin/reject-booking/<int:booking_id>", methods=["PUT"])
@jwt_required()
def reject_booking(booking_id):

    booking = Booking.query.get(booking_id)

    if not booking:
        return jsonify({
            "success": False,
            "message": "Booking not found."
        }), 404

    if booking.booking_status == "Cancelled":
        return jsonify({
            "success": False,
            "message": "Booking has already been cancelled."
        }), 400

    if booking.booking_status == "Completed":
        return jsonify({
            "success": False,
            "message": "Completed bookings cannot be rejected."
        }), 400

    trek = Trek.query.get(booking.trek_id)
    data = request.get_json()
    booking.booking_status = "Cancelled"
    booking.cancelled_at = datetime.utcnow()
    booking.cancellation_reason = data.get(
        "cancellation_reason",
        "Rejected by Admin"
    )
    booking.admin_remarks = data.get(
        "admin_remarks",
        "Booking Rejected"
    )

    # Refund
    if booking.payment_status == "Paid":
        booking.refund_status = "Pending"
        booking.refund_amount = booking.total_amount
        booking.refund_reason = "Booking Rejected by Admin"
    else:
        booking.refund_status = "Not Applicable"

    # Restore Slots    
    if trek:
        trek.available_slots += booking.number_of_people

    create_notification(

    receiver_id=booking.user_id,

    title="Booking Rejected",

    message="Your booking has been rejected by the administrator.",

    notification_type="Booking",

    related_booking_id=booking.id,

    related_trek_id=booking.trek_id

)

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Booking rejected successfully."
    }), 200

@api_bp.route("/api/admin/bookings/<int:booking_id>/status", methods=["PUT"])
def update_booking_status(booking_id):

    data = request.get_json()

    booking = Booking.query.get(booking_id)

    if not booking:
        return jsonify({
            "success": False,
            "message": "Booking not found."
        }), 404

    status = data.get("status")

    if status not in ["Accepted", "Rejected"]:
        return jsonify({
            "success": False,
            "message": "Invalid booking status."
        }), 400

    booking.booking_status = status
    db.session.commit()

    return jsonify({
        "success": True,
        "message": f"Booking {status.lower()} successfully."
    }), 200




# ADMIN BOOKINGS ENDS

# ADMIN STAFF STARTS
import random
import string

# GENERATE TEMP PASSWORD
characters = string.ascii_letters + string.digits + "@#$"

temporary_password = "".join(

    random.choice(characters)

    for _ in range(10)

)


# CREATE STAFF
@api_bp.route("/api/admin/create-staff", methods=["POST"])
def create_staff():

    data = request.get_json()
    print(data)

    # -----------------------------------------
    # CHECK EMAIL
    # -----------------------------------------

    if User.query.filter_by(email=data["email"]).first():

        return jsonify({

            "success": False,
            "message": "Email already exists."

        }),400

    # -----------------------------------------
    # CHECK MOBILE
    # -----------------------------------------

    if User.query.filter_by(
        mobile_number=data["mobile_number"]
    ).first():

        return jsonify({

            "success":False,
            "message":"Mobile number already exists."

        }),400

    # -----------------------------------------
    # GENERATE EMPLOYEE ID
    # -----------------------------------------

    last_staff = StaffProfile.query.order_by(
        StaffProfile.id.desc()
    ).first()

    if last_staff:

        employee_id = f"TMP{last_staff.id+1:03d}"

    else:

        employee_id = "TMP001"

    # -----------------------------------------
    # CREATE USER
    # -----------------------------------------

    user = User(

        full_name=data["full_name"],

        email=data["email"],

        mobile_number=data["mobile_number"],

        password_hash = generate_password_hash(temporary_password),

        date_of_birth=datetime.strptime(
            data["date_of_birth"],
            "%Y-%m-%d"
        ).date(),

        gender=data["gender"],

        city=data["city"],

        state=data["state"],

        emergency_contact_name=data["emergency_contact_name"],

        emergency_contact_number=data["emergency_contact_number"],

        role="staff",

        status="Active"

    )

    db.session.add(user)

    db.session.commit()

    # -----------------------------------------
    # CREATE STAFF PROFILE
    # -----------------------------------------

    staff = StaffProfile(

        user_id=user.id,

        employee_id=employee_id,

        profession=data["profession"],

        specialization=data["specialization"],

        experience_years=int(data["experience_years"]),

        certifications=data["certifications"],

        languages_known=data["languages_known"],

        emergency_contact_name=data["emergency_contact_name"],

        emergency_contact_number=data["emergency_contact_number"],

        address=data["address"],

        joining_date=datetime.strptime(

            data["joining_date"],

            "%Y-%m-%d"

        ).date(),

        availability=data["availability"],

        bio=data["bio"]

    )

    db.session.add(staff)

    db.session.commit()

    return jsonify({
        "success": True,

    "message": "Staff member created successfully.",

    "employee_id": employee_id,

    "staff_id": staff.id,

    "email": user.email,

    "temporary_password": temporary_password
    }),201


# ==========================================================
# GET ALL STAFF : admin
# ==========================================================

@api_bp.route("/api/admin/staff", methods=["GET"])
def get_all_staff():

    staff_profiles = StaffProfile.query.order_by(
        StaffProfile.joining_date.desc()
    ).all()

    staff_list = []

    for profile in staff_profiles:

        user = profile.user

        assignment_count = StaffAssignment.query.filter_by(
            staff_id=user.id
        ).count()

        staff_list.append({

            "id": user.id,

            "employee_id": profile.employee_id,

            "full_name": user.full_name,

            "email": user.email,

            "mobile_number": user.mobile_number,

            "profile_picture": user.profile_picture,

            "city": user.city,

            "state": user.state,

            "account_status": user.status,          # User account status

    "availability": profile.availability,   # Staff availability

            "profession": profile.profession,

            "specialization": profile.specialization,

            "experience_years": profile.experience_years,

            "availability": profile.availability,

            "joining_date": profile.joining_date.strftime("%d %b %Y"),

            "assigned_treks": assignment_count

        })

    return jsonify({

        "success": True,

        "count": len(staff_list),

        "data": staff_list

    })

# see each staff one by one: admin
# ==========================================================
# ADMIN VIEW STAFF
# ==========================================================

@api_bp.route("/api/admin/staff/<int:staff_id>", methods=["GET"])
def admin_view_staff(staff_id):

    user = User.query.get_or_404(staff_id)

    profile = StaffProfile.query.filter_by(
        user_id=user.id
    ).first_or_404()

    # ======================================================
    # ASSIGNED TREKS
    # ======================================================

    assignments = StaffAssignment.query.filter_by(
        staff_id=user.id
    ).order_by(
        StaffAssignment.assigned_date.desc()
    ).all()

    assigned_treks = []

    completed = 0
    ongoing = 0
    upcoming = 0

    for assignment in assignments:

        trek = assignment.trek

        assigned_treks.append({

            "assignment_id": assignment.id,

            "trek_id": trek.id,

            "trek_name": trek.trek_name,

            "location": trek.location,

            "difficulty": trek.difficulty,

            "trek_status": trek.status,

            "role_in_trek": assignment.role_in_trek,

            "assignment_status": assignment.assignment_status,

            "assigned_date": assignment.assigned_date.strftime("%d %b %Y"),

            "remarks": assignment.remarks

        })

        if trek.status == "Completed":
            completed += 1

        elif trek.status == "Ongoing":
            ongoing += 1

        elif trek.status == "Upcoming":
            upcoming += 1

    # ======================================================
    # RESPONSE
    # ======================================================

    return jsonify({

        "success": True,

        "data": {

            "staff": {

                "id": user.id,

                "employee_id": profile.employee_id,

                "full_name": user.full_name,

                "email": user.email,

                "mobile_number": user.mobile_number,

                "profile_picture": user.profile_picture,

                "gender": user.gender,

                "date_of_birth": user.date_of_birth.strftime("%Y-%m-%d"),

                "city": user.city,

                "state": user.state,

                "account_status": user.status,

                "profession": profile.profession,

                "specialization": profile.specialization,

                "experience_years": profile.experience_years,

                "availability": profile.availability,

                "joining_date": profile.joining_date.strftime("%d %b %Y"),

                "languages_known": profile.languages_known,

                "certifications": profile.certifications,

                "bio": profile.bio,

                "address": profile.address,

                "emergency_contact_name": profile.emergency_contact_name,

                "emergency_contact_number": profile.emergency_contact_number

            },

            "summary": {

                "total_assigned": len(assignments),

                "completed": completed,

                "ongoing": ongoing,

                "upcoming": upcoming

            },

            "assignments": assigned_treks

        }

    })

# ==========================================================
# ASSIGN STAFF TO TREK: admin
# ==========================================================

@api_bp.route("/api/admin/assign-staff", methods=["POST"])
def assign_staff_to_trek():

    data = request.get_json()

    # --------------------------------------------------
    # CHECK STAFF
    # --------------------------------------------------

    user = User.query.filter_by(
        id=data["staff_id"],
        role="staff"
    ).first()

    if not user:

        return jsonify({

            "success": False,
            "message": "Staff member not found."

        }),404

    profile = user.staff_profile

    # --------------------------------------------------
    # CHECK TREK
    # --------------------------------------------------

    trek = Trek.query.get(data["trek_id"])

    if not trek:

        return jsonify({

            "success": False,
            "message": "Trek not found."

        }),404

    # --------------------------------------------------
    # CHECK IF TREK ALREADY HAS STAFF
    # --------------------------------------------------

    existing_assignment = StaffAssignment.query.filter_by(

        trek_id=trek.id

    ).first()

    if existing_assignment:

        return jsonify({

            "success": False,
            "message": "This trek already has a staff member assigned."

        }),400

    # --------------------------------------------------
    # CREATE ASSIGNMENT
    # --------------------------------------------------

    assignment = StaffAssignment(

        staff_id=user.id,

        trek_id=trek.id,

        role_in_trek=profile.profession,

        assignment_status="Assigned",

        remarks=data.get("remarks","")

    )

    db.session.add(assignment)
    create_notification(

    receiver_id=user.id,

    title="New Trek Assigned",

    message=f"You have been assigned to {trek.trek_name}.",

    notification_type="Assignment",

    related_trek_id=trek.id
    )


    db.session.commit()
    print("Assignment Created")
    print("Staff:", user.id)
    print("Trek:", trek.id)
    print("Assignment ID:", assignment.id)

    # --------------------------------------------------
    # RESPONSE
    # --------------------------------------------------

    return jsonify({

        "success": True,

        "message": "Staff assigned successfully."

    }),201


# ==========================================================
# REMOVE STAFF ASSIGNMENT: admin
# ==========================================================

@api_bp.route("/api/admin/assign-staff/<int:assignment_id>", methods=["DELETE"])
def remove_staff_assignment(assignment_id):

    assignment = StaffAssignment.query.get(assignment_id)

    if not assignment:

        return jsonify({

            "success": False,
            "message": "Assignment not found."

        }),404

    db.session.delete(assignment)

    db.session.commit()

    return jsonify({

        "success": True,
        "message": "Staff assignment removed successfully."

    })

# ==========================================================
# GET STAFF + AVAILABLE TREKS: assigning treks to staff: admin
# ==========================================================

@api_bp.route("/api/admin/assign-staff/<int:staff_id>", methods=["GET"])
def get_staff_assignment_data(staff_id):

    # -----------------------------------------
    # FIND STAFF
    # -----------------------------------------

    user = User.query.filter_by(
        id=staff_id,
        role="staff"
    ).first()

    if not user:

        return jsonify({

            "success": False,
            "message": "Staff member not found."

        }),404

    profile = user.staff_profile

    # -----------------------------------------
    # STAFF DETAILS
    # -----------------------------------------

    staff_data = {

        "id": user.id,

        "employee_id": profile.employee_id,

        "full_name": user.full_name,

        "email": user.email,

        "mobile_number": user.mobile_number,

        "profession": profile.profession,

        "specialization": profile.specialization,

        "experience_years": profile.experience_years,

        "availability": profile.availability,

        "joining_date": profile.joining_date.strftime("%d %b %Y")

    }

    # -----------------------------------------
    # TREKS ALREADY ASSIGNED
    # -----------------------------------------

    assigned_ids = db.session.query(
        StaffAssignment.trek_id
    ).all()

    assigned_ids = [trek_id for (trek_id,) in assigned_ids]

    # -----------------------------------------
    # AVAILABLE TREKS
    # -----------------------------------------

    treks = Trek.query.filter(

        Trek.status != "Completed",

        ~Trek.id.in_(assigned_ids)

    ).order_by(Trek.start_date).all()

    available_treks = []

    for trek in treks:

        available_treks.append({

            "id": trek.id,

            "trek_name": trek.trek_name,

            "location": trek.location,

            "difficulty": trek.difficulty,

            "start_date": trek.start_date.strftime("%d %b %Y"),

            "end_date": trek.end_date.strftime("%d %b %Y")

        })

    # -----------------------------------------
    # CURRENT ASSIGNMENTS OF THIS STAFF
    # -----------------------------------------

    assignments = StaffAssignment.query.filter_by(

        staff_id=user.id

    ).all()

    assigned_treks = []

    for assignment in assignments:

        trek = assignment.trek

        assigned_treks.append({

            "assignment_id": assignment.id,

            "trek_name": trek.trek_name,

            "location": trek.location,

            "role": assignment.role_in_trek,

            "assigned_date": assignment.assigned_date.strftime("%d %b %Y"),

            "status": assignment.assignment_status

        })

    return jsonify({

        "success": True,

        "data": {

            "staff": staff_data,

            "available_treks": available_treks,

            "assigned_treks": assigned_treks

        }

    })
# ADMIN STAFF ENDS

# STAFF STARTS
# ==========================================================
# STAFF - GET ASSIGNED TREKS: staff
# ==========================================================

@api_bp.route("/api/staff/treks/<int:staff_id>", methods=["GET"])
def get_staff_treks(staff_id):

    assignments = StaffAssignment.query.filter_by(
        staff_id=staff_id
    ).all()

    treks = []

    for assignment in assignments:

        trek = Trek.query.get(assignment.trek_id)

        if not trek:
            continue

        booking_count = Booking.query.filter_by(
            trek_id=trek.id
        ).count()

        treks.append({

            "id": trek.id,

            "trek_name": trek.trek_name,

            "trek_type": trek.trek_type,

            "location": trek.location,

            "state": trek.state,

            "difficulty": trek.difficulty,

            "duration": trek.duration,

            "price": trek.price,

            "capacity": trek.capacity,

            "available_slots": trek.available_slots,

            "cover_image": trek.cover_image,

            "start_date": trek.start_date.strftime("%d %b %Y"),

            "end_date": trek.end_date.strftime("%d %b %Y"),

            "status": trek.status,

            "booking_count": booking_count,

            "assigned_role": assignment.role_in_trek,

            "assignment_status": assignment.assignment_status,
            "assignment_id": assignment.id

        })

    return jsonify({

        "success": True,

        "count": len(treks),

        "data": treks

    })

# TREK IS COMPLETED
@api_bp.route("/api/staff/treks/<int:trek_id>/details", methods=["GET"])
@jwt_required()
def get_staff_trek_details(trek_id):

    staff_id = int(get_jwt_identity())
    assignment = StaffAssignment.query.filter_by(
        trek_id=trek_id,
        staff_id=staff_id
    ).first()

    if not assignment:
        return jsonify({
            "success": False,
            "message": "This trek is not assigned to you."
        }), 403

    trek = Trek.query.get_or_404(trek_id)

    gallery = [{
        "id": media.id,
        "media_type": media.media_type,
        "media_url": media.media_url,
        "caption": media.caption
    } for media in trek.media]

    trek_data = {
        "id": trek.id,
        "trek_name": trek.trek_name,
        "trek_type": trek.trek_type,
        "location": trek.location,
        "meeting_point": trek.meeting_point,
        "state": trek.state,
        "difficulty": trek.difficulty,
        "emergency_level": trek.emergency_level,
        "duration": trek.duration,
        "price": trek.price,
        "description": trek.description,
        "organizer": trek.organizer,
        "capacity": trek.capacity,
        "available_slots": trek.available_slots,
        "cover_image": trek.cover_image,
        "minimum_age": trek.minimum_age,
        "maximum_age": trek.maximum_age,
        "fitness_requirement": trek.fitness_requirement,
        "equipment_required": trek.equipment_required,
        "start_date": trek.start_date,
        "end_date": trek.end_date,
        "registration_deadline": trek.registration_deadline,
        "status": trek.status
    }

    return jsonify({
        "success": True,
        "data": {
            "trek": trek_data,
            "gallery": gallery,
            "assignment": {
                "id": assignment.id,
                "role": assignment.role_in_trek,
                "status": assignment.assignment_status
            }
        }
    })

@api_bp.route("/api/staff/complete-trek/<int:assignment_id>", methods=["PUT"])
@jwt_required()
def complete_trek(assignment_id):

    staff_id = int(get_jwt_identity())

    assignment = StaffAssignment.query.filter_by(
        id=assignment_id,
        staff_id=staff_id
    ).first()

    if not assignment:
        return jsonify({
            "success": False,
            "message": "Assignment not found."
        }),404

    if assignment.assignment_status == "Completed":
        return jsonify({
            "success": False,
            "message": "This trek has already been completed."
        }),400

    trek = Trek.query.get(assignment.trek_id)

    if not trek:
        return jsonify({
            "success": False,
            "message": "Trek not found."
        }),404

    assignment.assignment_status = "Completed"

    assignment.completed_at = datetime.utcnow()

    trek.status = "Completed"

    # ---------------------------------
    # Notify all booked users
    # ---------------------------------

    bookings = Booking.query.filter_by(
        trek_id=trek.id,
        booking_status="Accepted"
    ).all()

    for booking in bookings:

        create_notification(

            receiver_id=booking.user_id,

            title="Trek Completed",

            message=f"Congratulations! Your trek '{trek.trek_name}' has been marked as completed. We hope you enjoyed your adventure.",

            notification_type="Completion",

            related_booking_id=booking.id,

            related_trek_id=trek.id

        )

    # ---------------------------------
    # Notify Admins
    # ---------------------------------

    staff = User.query.get(staff_id)
    admins = User.query.filter_by(role="admin").all()

    for admin in admins:

        create_notification(

            receiver_id=admin.id,

            title="Trek Completed",

            message=f"{staff.full_name} has completed '{trek.trek_name}'.",

            notification_type="Completion",

            related_trek_id=trek.id

        )

    db.session.commit()

    return jsonify({

        "success": True,

        "message": "Trek marked as completed."

    }),200

# ======================================================
# STAFF PARTICIPANTS
# ======================================================

@api_bp.route("/api/staff/participants", methods=["GET"])
@jwt_required()
def staff_participants():

    staff_id = int(get_jwt_identity())

    assignments = StaffAssignment.query.filter_by(
        staff_id=staff_id
    ).all()

    trek_cards = []

    for assignment in assignments:

        trek = assignment.trek

        participants = []

        bookings = Booking.query.filter_by(
            trek_id=trek.id,
            booking_status="Accepted"
        ).all()

        from datetime import date
        for booking in bookings:

            user = booking.user

            participants.append({
    "id": user.id,
    "full_name": user.full_name,
    "email": user.email,
    "phone": user.mobile_number,
    "gender": user.gender,
    "age": date.today().year - user.date_of_birth.year,
    "booking_reference": booking.booking_reference,
    "people": booking.number_of_people,
    "booking_date": booking.booking_date.strftime("%d %b %Y")
})

        trek_cards.append({

            "id": trek.id,

            "trek_name": trek.trek_name,

            "location": trek.location,

            "cover_image": trek.cover_image,

            "start_date": trek.start_date.strftime("%d %b %Y"),

            "end_date": trek.end_date.strftime("%d %b %Y"),

            "participant_count": len(participants),

            "participants": participants

        })

    return jsonify({

        "success": True,

        "data": trek_cards

    })

# ======================================================
# STAFF SUMMARY
# ======================================================

@api_bp.route("/api/staff/summary", methods=["GET"])
@jwt_required()
def staff_summary():

    staff_id = int(get_jwt_identity())

    assignments = StaffAssignment.query.filter_by(
        staff_id=staff_id
    ).all()

    assigned_treks = len(assignments)

    completed_treks = 0
    upcoming_treks = 0
    ongoing_treks = 0

    total_participants = 0

    difficulty_chart = {
        "Easy":0,
        "Moderate":0,
        "Hard":0
    }

    status_chart = {
        "Upcoming":0,
        "Ongoing":0,
        "Completed":0,
        "Cancelled":0
    }

    assigned_trek_table = []

    recent_participants = []

    for assignment in assignments:

        trek = assignment.trek
        # New treks are stored as "Available" when created, while the staff
        # dashboard reports future treks as "Upcoming". Normalize that value
        # here so the counters and status chart stay accurate.
        trek_status = "Upcoming" if trek.status == "Available" else trek.status

        status_chart[trek_status] = status_chart.get(
            trek_status,
            0
        ) + 1

        if trek_status == "Completed":
            completed_treks += 1

        elif trek_status == "Upcoming":
            upcoming_treks += 1

        elif trek_status == "Ongoing":
            ongoing_treks += 1

        difficulty_chart[trek.difficulty] = difficulty_chart.get(
            trek.difficulty,
            0
        ) + 1

        bookings = Booking.query.filter_by(
            trek_id=trek.id,
            booking_status="Accepted"
        ).all()

        total_participants += len(bookings)

        assigned_trek_table.append({

            "id":trek.id,

            "trek_name":trek.trek_name,

            "location":trek.location,

            "status":trek_status,

            "participants":len(bookings),

            "start_date":trek.start_date.strftime("%d %b %Y")

        })

        for booking in bookings:

            recent_participants.append({

                "id":booking.id,

                "name":booking.user.full_name,

                "trek":trek.trek_name,

                "booking_date":booking.booking_date.strftime("%d %b %Y")

            })

    recent_participants = sorted(

        recent_participants,

        key=lambda x:x["booking_date"],

        reverse=True

    )[:5]

    return jsonify({

        "success":True,

        "data":{

            "summary":{

                "assigned_treks":assigned_treks,

                "completed_treks":completed_treks,

                "upcoming_treks":upcoming_treks,

                "ongoing_treks":ongoing_treks,

                "total_participants":total_participants

            },

            "status_chart":status_chart,

            "difficulty_chart":difficulty_chart,

            "assigned_trek_table":assigned_trek_table,

            "recent_participants":recent_participants

        }

    })
# STAFF ENDS


#  ADMIN USER STARTS
# ADMIN USERS DASHBOARD
@api_bp.route("/api/admin/users", methods=["GET"])
def get_all_users():
    users = User.query.filter_by(role="user").order_by(User.created_at.desc()).all()
    user_list = []
    for user in users:
        user_list.append({
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "mobile_number": user.mobile_number,
            "city": user.city,
            "state": user.state,
            "gender": user.gender,
            "status": user.status,
            "profile_picture": user.profile_picture,
            "created_at": user.created_at,
            "last_login": user.last_login
        })

    return jsonify({
        "success": True,
        "data": {
            "users": user_list
        }
    })

# REFUNDING 
@api_bp.route("/api/admin/process-refund/<int:booking_id>", methods=["PUT"])
@jwt_required()
def process_refund(booking_id):

    booking = Booking.query.get(booking_id)

    if not booking:
        return jsonify({
            "success": False,
            "message": "Booking not found."
        }), 404

    # -------------------------
    # Booking Validation
    # -------------------------

    if booking.booking_status != "Cancelled":
        return jsonify({
            "success": False,
            "message": "Only cancelled bookings can be refunded."
        }), 400

    if booking.payment_status != "Paid":
        return jsonify({
            "success": False,
            "message": "No payment found for this booking."
        }), 400

    if booking.refund_status == "Completed":
        return jsonify({
            "success": False,
            "message": "Refund has already been processed."
        }), 400

    data = request.get_json()

    # -------------------------
    # Process Refund
    # -------------------------

    booking.refund_status = "Completed"

    booking.refund_date = datetime.utcnow()

    booking.payment_status = "Refunded"

    booking.refund_amount = booking.total_amount

    booking.refund_reason = data.get(
        "refund_reason",
        "Refund processed successfully."
    )

    create_notification(

    receiver_id=booking.user_id,

    title="Refund Processed",

    message=f"₹{booking.refund_amount} has been refunded successfully.",

    notification_type="Refund",

    related_booking_id=booking.id,

    related_trek_id=booking.trek_id

)

    db.session.commit()

    return jsonify({

        "success": True,

        "message": "Refund processed successfully."

    }), 200
# ADMIN USER ENDS

# ==========================================================
# ADMIN SUMMARY
# ==========================================================

@api_bp.route("/api/admin/summary", methods=["GET"])
def admin_summary():

    # ======================================================
    # SUMMARY
    # ======================================================

    total_users = User.query.filter_by(role="user").count()

    total_staff = StaffProfile.query.count()

    total_treks = Trek.query.count()

    total_bookings = Booking.query.count()


    # ======================================================
    # BOOKING STATUS
    # ======================================================

    booking_chart = {

        "Pending": Booking.query.filter_by(
            booking_status="Pending"
        ).count(),

        "Accepted": Booking.query.filter_by(
            booking_status="Accepted"
        ).count(),

        "Rejected": Booking.query.filter_by(
            booking_status="Rejected"
        ).count(),

    }


    # ======================================================
    # TREK STATUS
    # ======================================================

    trek_chart = {

        "Upcoming": Trek.query.filter_by(
            status="Upcoming"
        ).count(),

        "Ongoing": Trek.query.filter_by(
            status="Ongoing"
        ).count(),

        "Completed": Trek.query.filter_by(
            status="Completed"
        ).count(),

        "Cancelled": Trek.query.filter_by(
            status="Cancelled"
        ).count()

    }


    # ======================================================
    # TREK DIFFICULTY
    # ======================================================

    difficulty_chart = {

        "Easy": Trek.query.filter_by(
            difficulty="Easy"
        ).count(),

        "Moderate": Trek.query.filter_by(
            difficulty="Moderate"
        ).count(),

        "Hard": Trek.query.filter_by(
            difficulty="Hard"
        ).count()

    }


    # ======================================================
    # STAFF PROFESSION
    # ======================================================

    professions = db.session.query(
        StaffProfile.profession,
        db.func.count(StaffProfile.id)
    ).group_by(
        StaffProfile.profession
    ).all()

    staff_chart = {

        profession:count

        for profession,count in professions

    }


    # ======================================================
    # TOP TREKS
    # ======================================================

    top_treks = []

    treks = Trek.query.all()

    treks = sorted(

        treks,

        key=lambda x: len(x.bookings),

        reverse=True

    )[:5]

    for trek in treks:

        top_treks.append({

            "id":trek.id,

            "trek_name":trek.trek_name,

            "location":trek.location,

            "cover_image":trek.cover_image,

            "price":trek.price,

            "duration":trek.duration,

            "difficulty":trek.difficulty,

            "capacity":trek.capacity,

            "available_slots":trek.available_slots,

            "booking_count":len(trek.bookings)

        })


    # ======================================================
    # TOP STAFF
    # ======================================================

    top_staff = []

    staff_members = StaffProfile.query.all()

    staff_members = sorted(

        staff_members,

        key=lambda x: len(x.user.staff_assignments),

        reverse=True

    )[:5]

    for profile in staff_members:

        top_staff.append({

            "id":profile.user.id,

            "employee_id":profile.employee_id,

            "full_name":profile.user.full_name,

            "profession":profile.profession,

            "availability":profile.availability,

            "assignment_count":len(profile.user.staff_assignments)

        })


    # ======================================================
    # RECENT BOOKINGS
    # ======================================================

    recent_bookings = []

    bookings = Booking.query.order_by(

        Booking.booking_date.desc()

    ).limit(5).all()

    for booking in bookings:

        recent_bookings.append({

            "id":booking.id,

            "booking_reference":booking.booking_reference,

            "user":booking.user.full_name,

            "trek":booking.trek.trek_name,

            "amount":booking.total_amount,

            "status":booking.booking_status

        })


    # ======================================================
    # RECENT USERS
    # ======================================================

    recent_users = []

    users = User.query.filter_by(

        role="user"

    ).order_by(

        User.created_at.desc()

    ).limit(5).all()

    for user in users:

        recent_users.append({

            "id":user.id,

            "full_name":user.full_name,

            "email":user.email,

            "joined":user.created_at.strftime("%d %b %Y")

        })

    # ======================================================
# TREK OVERVIEW TABLE
# ======================================================

    trek_table = []

    for trek in Trek.query.order_by(Trek.start_date).all():

        trek_table.append({

        "id": trek.id,

        "trek_name": trek.trek_name,

        "booked": trek.capacity - trek.available_slots,

        "capacity": trek.capacity,

        "available": trek.available_slots,

        "status": trek.status

    })
        
    # ======================================================
# STAFF SUMMARY TABLE
# ======================================================

    staff_table = []

    staff_profiles = StaffProfile.query.all()

    for profile in staff_profiles:

        staff_table.append({

        "id": profile.user.id,

        "employee_id": profile.employee_id,

        "name": profile.user.full_name,

        "profession": profile.profession,

        "assigned_treks": len(profile.user.staff_assignments),

        "availability": profile.availability

    })
        
    # ======================================================
# USER BOOKING SUMMARY TABLE
# ======================================================

    user_booking_table = []

    users = User.query.filter_by(role="user").all()

    for user in users:

        bookings = Booking.query.filter_by(user_id=user.id).all()

    total_spent = sum(b.total_amount for b in bookings)

    user_booking_table.append({

        "id": user.id,

        "full_name": user.full_name,

        "total_bookings": len(bookings),

        "accepted": sum(
            1 for b in bookings
            if b.booking_status == "Accepted"
        ),

        "pending": sum(
            1 for b in bookings
            if b.booking_status == "Pending"
        ),

        "rejected": sum(
            1 for b in bookings
            if b.booking_status == "Rejected"
        ),

        "total_spent": total_spent

    })

    # ======================================================
# REVENUE TREND (LAST 6 MONTHS)
# ======================================================

    from datetime import datetime

    current_month = datetime.now().month
    current_year = datetime.now().year

    months = OrderedDict()

    for i in range(5, -1, -1):

        month = current_month - i
    year = current_year

    while month <= 0:
        month += 12
        year -= 1

    month_name = datetime(year, month, 1).strftime("%b")

    months[(year, month)] = {
        "month": month_name,
        "revenue": 0
    }

    results = db.session.query(

    extract("year", Booking.booking_date),

    extract("month", Booking.booking_date),

    db.func.sum(Booking.total_amount)

).filter(

    Booking.booking_status == "Accepted"

).group_by(

    extract("year", Booking.booking_date),

    extract("month", Booking.booking_date)

).all()

    for year, month, revenue in results:

        key = (int(year), int(month))

    if key in months:

        months[key]["revenue"] = float(revenue or 0)

    revenue_chart = list(months.values())

    # TOP 5 MOST POPULAR TREKS
    most_popular_treks = []

    popular_treks = (
    db.session.query(
        Trek,
        db.func.count(Booking.id).label("booking_count")
    )
    .outerjoin(Booking, Trek.id == Booking.trek_id)
    .group_by(Trek.id)
    .order_by(db.desc("booking_count"))
    .limit(5)
    .all()
)

    for trek, booking_count in popular_treks:

        most_popular_treks.append({

        "id": trek.id,

        "trek_name": trek.trek_name,

        "cover_image": trek.cover_image,

        "location": trek.location,

        "price": trek.price,

        "booking_count": booking_count

    })

    # ======================================================
    # RESPONSE
    # ======================================================

    return jsonify({

        "success":True,

        "data":{

            "summary":{

                "total_users":total_users,

                "total_staff":total_staff,

                "total_treks":total_treks,

                "total_bookings":total_bookings

            },

            "booking_chart":booking_chart,

            "trek_chart":trek_chart,

            "difficulty_chart":difficulty_chart,

            "staff_chart":staff_chart,

            "top_treks":top_treks,

            "top_staff":top_staff,

            "recent_bookings":recent_bookings,

            "recent_users":recent_users,
            "trek_table": trek_table,
            "revenue_chart": revenue_chart,

"staff_table": staff_table,

"user_booking_table": user_booking_table,
"most_popular_treks": most_popular_treks

        }

    })



# USER STARTS
# USER DASHBOARD
@api_bp.route("/api/user/dashboard", methods=["GET"])
@jwt_required()
def user_dashboard():

    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "success": False,
            "message": "User not found."
        }), 404

    bookings = Booking.query.filter_by(user_id=user_id).all()

    total = len(bookings)
    pending = 0
    accepted = 0
    rejected = 0

    next_trek = None
    recent_bookings = []

    # ======================================================
    # BOOKINGS + STATS
    # ======================================================

    for booking in bookings:

        trek = Trek.query.get(booking.trek_id)

        if not trek:
            continue

        if booking.booking_status == "Pending":
            pending += 1

        elif booking.booking_status == "Accepted":
            accepted += 1

        elif booking.booking_status == "Rejected":
            rejected += 1


        recent_bookings.append({

            "booking_reference": booking.booking_reference,

            "trek_name": trek.trek_name,

            "cover_image": trek.cover_image,

            "location": trek.location,

            "start_date": trek.start_date.strftime("%d %b %Y"),

            "booking_status": booking.booking_status

        })

    # Latest 3 bookings
    recent_bookings = recent_bookings[::-1][:3]

    # ======================================================
    # NEXT TREK (Only Confirmed)
    # ======================================================

    accepted_bookings = [

        booking

        for booking in bookings

        if booking.booking_status == "Accepted"

    ]

    if accepted_bookings:

        upcoming_booking = sorted(

            accepted_bookings,

            key=lambda x: Trek.query.get(x.trek_id).start_date

        )[0]

        trek = Trek.query.get(upcoming_booking.trek_id)

        assignment = StaffAssignment.query.filter_by(

            trek_id=trek.id,

            assignment_status="Assigned"

        ).first()

        staff_name = "Not Assigned"

        if assignment:

            staff = User.query.get(assignment.staff_id)

            if staff:

                staff_name = staff.full_name

        next_trek = {

            "trek_id": trek.id,

            "trek_name": trek.trek_name,

            "cover_image": trek.cover_image,

            "location": trek.location,

            "difficulty": trek.difficulty,

            "start_date": trek.start_date.strftime("%d %b %Y"),

            "end_date": trek.end_date.strftime("%d %b %Y"),

            "staff_name": staff_name

        }

    # ======================================================
    # RECOMMENDED TREKS
    # ======================================================

    recommended = []

    treks = (

        Trek.query

        .filter(

            Trek.status == "Upcoming",

            Trek.available_slots > 0

        )

        .order_by(Trek.start_date)

        .limit(3)

        .all()

    )

    for trek in treks:

        recommended.append({

            "id": trek.id,

            "trek_name": trek.trek_name,

            "cover_image": trek.cover_image,

            "difficulty": trek.difficulty,

            "price": trek.price,

            "location": trek.location

        })

    # ======================================================
    # RESPONSE
    # ======================================================

    return jsonify({

        "success": True,

        "data": {

            "user_name": user.full_name,

            "stats": {

                "total": total,

                "pending": pending,

                "accepted": accepted,

                "rejected": rejected
            },

            "next_trek": next_trek,

            "recent_bookings": recent_bookings,

            "recommended": recommended

        }

    }), 200


# USER PROFILE
@api_bp.route("/api/user/profile", methods=["GET"])
@jwt_required()
def user_profile():

    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:

        return jsonify({
            "success": False,
            "message": "User not found."
        }),404

    return jsonify({

        "success":True,

        "data":{

            "id":user.id,

            "full_name":user.full_name,

            "email":user.email,

            "mobile_number":user.mobile_number,

            "date_of_birth":user.date_of_birth.strftime("%d %b %Y"),

            "gender":user.gender,

            "city":user.city,

            "state":user.state,

            "emergency_contact_name":user.emergency_contact_name,

            "emergency_contact_number":user.emergency_contact_number,

            "profile_picture":user.profile_picture

        }

    }),200


# EDITING USER PROFILE
@api_bp.route("/api/user/profile", methods=["PUT"])
@jwt_required()
def update_user_profile():

    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:

        return jsonify({

            "success":False,

            "message":"User not found."

        }),404

    data = request.form

    user.full_name = data.get("full_name")
    user.mobile_number = data.get("mobile_number")
    user.city = data.get("city")
    user.state = data.get("state")
    user.emergency_contact_name = data.get("emergency_contact_name")
    user.emergency_contact_number = data.get("emergency_contact_number")

    # --------------------------
    # Profile Picture
    image = request.files.get("profile_picture")
    if image:
        filename = secure_filename(image.filename)
        
        upload_folder = os.path.join(current_app.root_path, "static", "profile_uploads")
        os.makedirs(upload_folder, exist_ok=True)
        image.save(os.path.join(upload_folder, filename))
        user.profile_picture = filename
        db.session.commit()
        
        return jsonify({
            "success":True,
            "message":"Profile updated successfully."
        }),200


# USER BROWSE TREKS
@api_bp.route("/api/user/browse-treks", methods=["GET"])
@jwt_required()
@cache.cached(timeout=300, key_prefix="user-browse-treks")
def user_browse_treks():

    # ==========================================================
    # UPCOMING TREKS
    # ==========================================================

    treks = Trek.query.filter_by(
        status="Upcoming"
    ).order_by(
        Trek.start_date.asc()
    ).all()

    trek_list = []

    for trek in treks:
        trek_list.append({
            "id": trek.id,
            "trek_name": trek.trek_name,
            "trek_type": trek.trek_type,
            "location": trek.location,
            "meeting_point": trek.meeting_point,
            "state": trek.state,
            "difficulty": trek.difficulty,
            "duration": trek.duration,
            "price": trek.price,
            "capacity": trek.capacity,
            "available_slots": trek.available_slots,
            "cover_image": trek.cover_image or "/images/default_trek.jpg",
            "description": trek.description,
            "organizer": trek.organizer,
            "start_date": trek.start_date.strftime("%d %b %Y"),
            "end_date": trek.end_date.strftime("%d %b %Y"),
            "status": trek.status
        })

    # ==========================================================
    # FILTERS
    # ==========================================================

    states = sorted({
        trek.state
        for trek in treks
    })

    difficulties = sorted({
        trek.difficulty
        for trek in treks
    })

    # ==========================================================
    # RESPONSE
    # ==========================================================

    return jsonify({
        "success": True,
        "data": {
            "treks": trek_list,
            "filters": {
                "states": states,
                "difficulties": difficulties
            }
        }
    }), 200


# USER VIEW EACH TREK
@api_bp.route("/api/user/view-trek/<int:trek_id>", methods=["GET"])
@jwt_required()
def user_view_trek(trek_id):

    trek = Trek.query.get(trek_id)
    if not trek:
        return jsonify({
            "success": False,
            "message": "Trek not found."
        }), 404

    gallery = []
    for media in trek.media:
        gallery.append({
            "id": media.id,
            "media_type": media.media_type,
            "media_url": media.media_url,
            "caption": media.caption
        })

    assignment = StaffAssignment.query.filter_by( trek_id=trek.id, assignment_status="Assigned").first()
    staff_data = None
    if assignment:
        profile = StaffProfile.query.filter_by(
            user_id=assignment.staff_id
        ).first()

        user = User.query.get(assignment.staff_id)

        if user and profile:
            staff_data = {
                "full_name": user.full_name,
                "profession": profile.profession,
                "experience_years": profile.experience_years,
                "role_in_trek": assignment.role_in_trek
            }
        else:
            staff_data = {
                "full_name": "No Staff Assigned",
                "profession": "-",
                "experience_years": "-",
                "role_in_trek": "-"
            }
    else:
        staff_data = {
            "full_name": "No Staff Assigned",
            "profession": "-",
            "experience_years": "-",
            "role_in_trek": "-"
        }

    return jsonify({
        "success": True,
        "data": {
            "id": trek.id,
            "trek_name": trek.trek_name,
            "trek_type": trek.trek_type,
            "location": trek.location,
            "meeting_point": trek.meeting_point,
            "state": trek.state,
            "difficulty": trek.difficulty,
            "emergency_level": trek.emergency_level,
            "duration": trek.duration,
            "price": trek.price,
            "description": trek.description,
            "organizer": trek.organizer,
            "capacity": trek.capacity,
            "available_slots": trek.available_slots,
            "cover_image": trek.cover_image,
            "minimum_age": trek.minimum_age,
            "maximum_age": trek.maximum_age,
            "fitness_requirement": trek.fitness_requirement,
            "equipment_required": trek.equipment_required,
            "staff": staff_data,
            "start_date": trek.start_date.strftime("%d %b %Y"),
            "end_date": trek.end_date.strftime("%d %b %Y"),
            "registration_deadline": trek.registration_deadline.strftime("%d %b %Y"),
            "status": trek.status,
            "gallery": gallery,
        }
    }), 200


# USER BOOK TREK
@api_bp.route("/api/user/book-trek", methods=["POST"])
@jwt_required()
def book_trek():
    user_id = get_jwt_identity()
    data = request.get_json()
    trek = Trek.query.get(data["trek_id"])

    if not trek:
        return jsonify({
            "success": False,
            "message": "Trek not found."
        }), 404

    # Check Trek Status
    if trek.status != "Upcoming":
        return jsonify({
            "success": False,
            "message": "This trek is no longer accepting bookings."
        }), 400
    
    # Duplicate Booking Check
    existing_booking = Booking.query.filter_by(
        user_id=user_id,
        trek_id=trek.id
    ).filter(
        Booking.booking_status.in_(
            ["Pending", "Accepted"]
        )
    ).first()

    if existing_booking:
        return jsonify({
        "success": False,
        "message": "You have already booked this trek."
    }), 400
    
    # Trek Full
    if trek.available_slots <= 0:
        return jsonify({
            "success": False,
            "message": "This trek is fully booked."
        }), 400

    # Check Available Slots
    if data["number_of_people"] > trek.available_slots:
        return jsonify({
            "success": False,
            "message": "Not enough slots available."
        }), 400
    
    # Participant Validation
    participants = data.get("participant_details", [])
    if data["number_of_people"] < 1:
        return jsonify({
            "success": False,
            "message": "At least one participant is required."
        }), 400

    if len(participants) != data["number_of_people"]:
        return jsonify({
            "success": False,
            "message": "Participant details are incomplete."
        }), 400

    for participant in participants:
        if not participant.get("full_name"):
            return jsonify({
                "success": False,
                "message": "Participant name is required."
            }), 400

        if not participant.get("age"):
            return jsonify({
                "success": False,
                "message": "Participant age is required."
            }), 400

        if not participant.get("gender"):
            return jsonify({
                "success": False,
                "message": "Participant gender is required."
            }), 400
        
        if not participant.get("mobile_number"):
            return jsonify({
                "success": False,
                "message": "Participant mobile number is required."
            }), 400

    # Validate Participant Ages
    for participant in data["participant_details"]:
        age = int(participant["age"])
        
        if trek.minimum_age and age < trek.minimum_age:
            return jsonify({
                "success": False,
                "message": f"Minimum age for this trek is {trek.minimum_age} years."
            }), 400

        if trek.maximum_age and age > trek.maximum_age:
            return jsonify({
                "success": False,
                "message": f"Maximum age for this trek is {trek.maximum_age} years."
            }), 400

    booking_reference = f"TM{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"

    # Create Booking
    booking = Booking(

    booking_reference=booking_reference,

    user_id=user_id,

    trek_id=trek.id,

    number_of_people=data["number_of_people"],

    participant_details=json.dumps(
        data["participant_details"]
    ),

    special_requests=data.get("special_requests"),

    total_amount=trek.price * data["number_of_people"],

    # -------------------------
    # Booking Status
    # -------------------------

    booking_status="Pending",

    # -------------------------
    # Payment
    # -------------------------

    payment_status="Pending",

    payment_method=None,

    payment_gateway=None,

    payment_reference=None,

    payment_date=None,

    # -------------------------
    # Approval
    # -------------------------

    approved_at=None,

    approved_by=None,

    admin_remarks=None,

    # -------------------------
    # Cancellation
    # -------------------------

    cancelled_at=None,

    cancellation_reason=None,

    # -------------------------
    # Refund
    # -------------------------

    refund_status="Not Applicable",

    refund_amount=0,

    refund_reason=None,

    refund_date=None

)

    db.session.add(booking)

    admins = User.query.filter_by(role="admin").all()

    for admin in admins:
       create_notification(
        receiver_id=admin.id,
        title="New Booking",
        message=f"{booking.user.full_name} booked {trek.trek_name}.",
        notification_type="Booking",
        related_booking_id=booking.id,
        related_trek_id=trek.id
    )

    trek.available_slots -= data["number_of_people"]

    create_notification(
    receiver_id=user_id,
    title="Booking Successful",
    message=f"Your booking for {trek.trek_name} has been received.",
    notification_type="Booking",
    related_booking_id=booking.id,
    related_trek_id=trek.id
)

    db.session.commit()

    return jsonify({

        "success": True,

        "message": "Booking Successful",

        "booking_reference": booking_reference

    }), 201

# SEE YOUR BOOKINGS: USER
@api_bp.route("/api/user/my-bookings", methods=["GET"])
@jwt_required()
def user_my_bookings():
    user_id = get_jwt_identity()

    bookings = (
        Booking.query
        .filter_by(user_id=user_id)
        .order_by(Booking.booking_date.desc())
        .all()
    )

    booking_list = []
    total = len(bookings)

    pending = 0
    accepted = 0
    cancelled = 0
    rejected = 0
    upcoming = 0
    completed = 0
    from datetime import datetime, date
    today = date.today()

    for booking in bookings:

        trek = Trek.query.get(booking.trek_id)

        if not trek:
            continue

        if booking.booking_status == "Pending":
            pending += 1

        elif booking.booking_status == "Accepted":
            accepted += 1

            if trek.start_date > today:
                upcoming += 1

            elif trek.end_date < today:
                completed += 1

        elif booking.booking_status == "Cancelled":
            cancelled += 1

        elif booking.booking_status == "Rejected":
                rejected += 1

        booking_list.append({
            "id": booking.id,
            "booking_reference": booking.booking_reference,
            "booking_date": booking.booking_date.strftime("%d %b %Y"),
            "booking_status": booking.booking_status,
            "payment_status": booking.payment_status,
            "number_of_people": booking.number_of_people,
            "total_amount": booking.total_amount,
            "trek_id": trek.id,
            "trek_name": trek.trek_name,
            "difficulty": trek.difficulty,
            "cover_image": trek.cover_image,
            "location": trek.location,
            "state": trek.state,
            "start_date": trek.start_date.strftime("%d %b %Y"),
            "end_date": trek.end_date.strftime("%d %b %Y")
        })

    return jsonify({
        "success": True,

        "data": {
            "stats": {
                "total": total,
                "pending": pending,
                "accepted": accepted,
                "rejected": rejected,
                "cancelled": cancelled,
                "upcoming": upcoming,
                "completed": completed
            },
            "bookings": booking_list
        }
    }), 200

# MAKING PAYMENT
@api_bp.route("/api/user/pay-booking/<int:booking_id>", methods=["PUT"])
@jwt_required()
def pay_booking(booking_id):

    user_id = get_jwt_identity()

    booking = Booking.query.filter_by(
        id=booking_id,
        user_id=user_id
    ).first()

    if not booking:
        return jsonify({
            "success": False,
            "message": "Booking not found."
        }),404

    if booking.payment_status == "Paid":
        return jsonify({
            "success": False,
            "message": "Payment has already been completed."
        }),400

    if booking.booking_status == "Cancelled":
        return jsonify({
            "success": False,
            "message": "Cancelled bookings cannot be paid."
        }),400

    data = request.get_json()

    payment_method = data.get("payment_method")

    if not payment_method:
        return jsonify({
            "success": False,
            "message": "Please select a payment method."
        }),400

    # -------------------------
    # Simulated Payment
    # -------------------------

    booking.payment_status = "Paid"

    booking.payment_method = payment_method

    booking.payment_gateway = "Demo Gateway"

    booking.payment_reference = (
        f"PAY{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
    )

    booking.payment_date = datetime.utcnow()

    create_notification(

    receiver_id=user_id,

    title="Payment Successful",

    message=f"Payment received for {booking.booking_reference}.",

    notification_type="Payment",

    related_booking_id=booking.id,

    related_trek_id=booking.trek_id

)
    admins = User.query.filter_by(role="admin").all()

    for admin in admins:
        create_notification(
        receiver_id=admin.id,
        title="Payment Received",
        message=f"{booking.user.full_name} paid for {booking.trek.trek_name}.",
        notification_type="Payment",
        related_booking_id=booking.id,
        related_trek_id=booking.trek_id
    )

    db.session.commit()

    return jsonify({

        "success": True,

        "message": "Payment Successful.",

        "payment_reference": booking.payment_reference

    }),200



# CANCEL BOOKING
@api_bp.route("/api/user/cancel-booking/<int:booking_id>", methods=["PUT"])
@jwt_required()
def cancel_booking(booking_id):
    user_id = get_jwt_identity()
    booking = Booking.query.filter_by(
        id=booking_id,
        user_id=user_id
    ).first()

    if not booking:
        return jsonify({
            "success": False,
            "message": "Booking not found."
        }), 404

    if booking.booking_status == "Cancelled":
        return jsonify({
            "success": False,
            "message": "Booking has already been cancelled."
        }), 400

    if booking.booking_status == "Completed":
        return jsonify({
            "success": False,
            "message": "Completed bookings cannot be cancelled."
        }), 400

    trek = Trek.query.get(booking.trek_id)
    data = request.get_json()
    booking.booking_status = "Cancelled"
    booking.cancelled_at = datetime.utcnow()
    booking.cancellation_reason = data.get(
        "cancellation_reason",
        "Cancelled by User"
    )

    # Refund
    if booking.payment_status == "Paid":
        booking.refund_status = "Pending"
        booking.refund_amount = booking.total_amount
        booking.refund_reason = "User Cancellation"
    else:
        booking.refund_status = "Not Applicable"

    # Restore Trek Slots
    if trek:
        trek.available_slots += booking.number_of_people

    create_notification(

    receiver_id=booking.user_id,

    title="Booking Cancelled",

    message="Your booking has been cancelled successfully.",

    notification_type="Booking",

    related_booking_id=booking.id,

    related_trek_id=booking.trek_id

)
    
    admins = User.query.filter_by(role="admin").all()

    for admin in admins:
       create_notification(
        receiver_id=admin.id,
        title="Booking Cancelled",
        message=f"{booking.user.full_name} cancelled {booking.trek.trek_name}.",
        notification_type="Booking",
        related_booking_id=booking.id,
        related_trek_id=booking.trek_id
    )

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Booking cancelled successfully."
    }), 200
# USER ENDS









# NOTIFICATION
def create_notification(
    receiver_id,
    title,
    message,
    notification_type,
    related_booking_id=None,
    related_trek_id=None,
    priority="Normal",
    expires_at=None
):

    notification = Notification(

        receiver_id=receiver_id,

        title=title,

        message=message,

        notification_type=notification_type,

        related_booking_id=related_booking_id,

        related_trek_id=related_trek_id,

        priority=priority,

        expires_at=expires_at,

        created_at=datetime.utcnow()

    )

    db.session.add(notification)

# GET ALL NOTIFICATIONS
@api_bp.route("/api/notifications", methods=["GET"])
@jwt_required()
def get_notifications():

    user_id = get_jwt_identity()

    notifications = Notification.query.filter_by(
        receiver_id=user_id
    ).order_by(
        Notification.created_at.desc()
    ).all()

    data = []

    for notification in notifications:

        data.append({

            "id": notification.id,

            "title": notification.title,

            "message": notification.message,

            "notification_type": notification.notification_type,

            "priority": notification.priority,

            "is_read": notification.is_read,

            "created_at": notification.created_at.strftime("%d %b %Y %I:%M %p")

        })

    return jsonify({

        "success": True,

        "notifications": data

    }),200

# UNREAD NOTIFICATIONS COUNT
@api_bp.route("/api/notifications/unread-count", methods=["GET"])
@jwt_required()
def unread_notification_count():

    user_id = get_jwt_identity()

    count = Notification.query.filter_by(

        receiver_id=user_id,

        is_read=False

    ).count()

    return jsonify({

        "success": True,

        "count": count

    }),200

# MARK THE READ NOTIFICATION
@api_bp.route("/api/notifications/<int:notification_id>/read", methods=["PUT"])
@jwt_required()
def mark_notification_read(notification_id):

    user_id = get_jwt_identity()

    notification = Notification.query.filter_by(

        id=notification_id,

        receiver_id=user_id

    ).first()

    if not notification:

        return jsonify({

            "success": False,

            "message": "Notification not found."

        }),404

    notification.is_read = True

    db.session.commit()

    return jsonify({

        "success": True,

        "message": "Notification marked as read."

    }),200

# ALL NOTIFICATIONS READ
@api_bp.route("/api/notifications/read-all", methods=["PUT"])
@jwt_required()
def mark_all_notifications_read():

    user_id = get_jwt_identity()

    notifications = Notification.query.filter_by(

        receiver_id=user_id,

        is_read=False

    ).all()

    for notification in notifications:

        notification.is_read = True

    db.session.commit()

    return jsonify({

        "success": True,

        "message": "All notifications marked as read."

    }),200


# user export route
@api_bp.route("/api/user/export-bookings", methods=["POST"])
@jwt_required()
def export_history():

    from tasks import export_booking_csv

    user_id = get_jwt_identity()

    task = export_booking_csv.delay(user_id)

    return jsonify({
        "success": True,
        "message": "Booking-history export started. You will be alerted when it is ready.",
        "task_id": task.id
    }), 202


@api_bp.route("/api/user/export-bookings/<task_id>", methods=["GET"])
@jwt_required()
def export_history_status(task_id):
    result = current_app.extensions["celery"].AsyncResult(task_id)

    if result.state == "FAILURE":
        return jsonify({
            "success": False,
            "state": result.state,
            "message": "Booking-history export failed. Please try again."
        }), 500

    return jsonify({
        "success": True,
        "state": result.state,
        "completed": result.state == "SUCCESS",
        "message": (
            "Your booking-history CSV has been emailed to you."
            if result.state == "SUCCESS"
            else "Your booking-history CSV is being prepared."
        )
    })
