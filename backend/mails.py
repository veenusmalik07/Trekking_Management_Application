from flask_mail import Message
from extensions import mail


def send_email(receiver_email, subject, body):

    msg = Message(
        subject=subject,
        recipients=[receiver_email],
        body=body
    )

    mail.send(msg)