from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# USER MODEL
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mobile_number = db.Column(db.String(15), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    emergency_contact_name = db.Column(db.String(100), nullable=False)
    emergency_contact_number = db.Column(db.String(15), nullable=False)
    profile_picture = db.Column(db.String(255), default='default_profile.png')
    role = db.Column(db.String(20), nullable=False, default='user')
    status = db.Column(db.String(20), nullable=False, default='Active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    # Relationships
    bookings = db.relationship("Booking", foreign_keys="Booking.user_id", backref="user", lazy=True)
    staff_profile = db.relationship('StaffProfile', backref='user', uselist=False)
    staff_assignments = db.relationship("StaffAssignment", backref="staff", cascade="all, delete-orphan", passive_deletes=True)
    notifications = db.relationship("Notification", backref="receiver", cascade="all, delete-orphan", lazy=True)


# TREK MODEL
class Trek(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trek_name = db.Column(db.String(150), nullable=False)
    trek_type = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    meeting_point = db.Column(db.String(200), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(30), nullable=False)
    emergency_level = db.Column(db.String(30),  nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    organizer = db.Column(db.String(150), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    available_slots = db.Column(db.Integer, nullable=False)
    cover_image = db.Column(db.String(255))
    minimum_age = db.Column(db.Integer)
    maximum_age = db.Column(db.Integer)
    fitness_requirement = db.Column(db.String(100))
    equipment_required = db.Column(db.Text)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    registration_deadline = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(30), default="Available")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    average_rating = db.Column(db.Float, default=0)
    total_ratings = db.Column(db.Integer, default=0)

    # RELATIONSHIPS
    bookings = db.relationship("Booking", foreign_keys="Booking.trek_id", backref="trek", lazy=True)
    staff_assignments = db.relationship( "StaffAssignment", backref="trek", cascade="all, delete-orphan", passive_deletes=True)
    media = db.relationship("TrekMedia", backref="trek", cascade="all, delete-orphan", lazy=True)


# TREK MEDIA MODEL
class TrekMedia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trek_id = db.Column(db.Integer, db.ForeignKey("trek.id", ondelete="CASCADE"), nullable=False)
    media_type = db.Column(db.String(20), nullable=False)   # Image / Video
    media_url = db.Column(db.String(255), nullable=False)
    caption = db.Column(db.String(255))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)


# BOOKING MODEL
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booking_reference = db.Column(db.String(30), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    trek_id = db.Column(db.Integer, db.ForeignKey('trek.id', ondelete="CASCADE"), nullable=False)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    number_of_people = db.Column(db.Integer, nullable=False)
    participant_details = db.Column(db.Text) 
    special_requests = db.Column(db.Text)
    total_amount = db.Column(db.Float, nullable=False)
    booking_status = db.Column(db.String(30), default="Pending")
    refund_date = db.Column(db.DateTime)
    refund_status = db.Column(db.String(30), nullable=False, default="Not Applicable")
    payment_date = db.Column(db.DateTime)
    payment_method = db.Column(db.String(30))
    payment_status = db.Column(db.String(30), default="Pending")
    cancelled_at = db.Column(db.DateTime)
    admin_remarks = db.Column(db.Text) 
    refund_amount = db.Column(db.Float, default=0)
    refund_reason = db.Column(db.Text)
    cancellation_reason = db.Column(db.Text)
    payment_reference = db.Column(db.String(100))
    payment_gateway = db.Column(db.String(30))
    approved_at = db.Column(db.DateTime)
    approved_by = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))
    approved_admin = db.relationship("User", foreign_keys=[approved_by])
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# STAFF PROFILE MODEL
class StaffProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    employee_id = db.Column(db.String(20), unique=True, nullable=False)
    profession = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(200), nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)
    certifications = db.Column(db.Text)
    languages_known = db.Column(db.String(200))
    emergency_contact_name = db.Column(db.String(100), nullable=False)
    emergency_contact_number = db.Column(db.String(15), nullable=False)
    address = db.Column(db.Text, nullable=False)
    joining_date = db.Column(db.Date, nullable=False)
    availability = db.Column(db.String(30), default="Available")
    bio = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 


# STAFF ASSIGNMENT MODEL
class StaffAssignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    trek_id = db.Column(db.Integer, db.ForeignKey('trek.id', ondelete="CASCADE"), nullable=False)
    role_in_trek = db.Column(db.String(100), nullable=False)
    assigned_date = db.Column(db.DateTime, default=datetime.utcnow)
    assignment_status = db.Column(db.String(30), default="Assigned")
    remarks = db.Column(db.Text)
    completed_at = db.Column(db.DateTime)


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    receiver_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)
    notification_type = db.Column(db.String(40), nullable=False)
    related_booking_id = db.Column(db.Integer, db.ForeignKey("booking.id"))
    related_trek_id = db.Column(db.Integer, db.ForeignKey("trek.id"))
    is_read = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(20), default="Normal")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime)
    booking = db.relationship("Booking", backref="notifications")
    trek = db.relationship("Trek", backref="notifications")