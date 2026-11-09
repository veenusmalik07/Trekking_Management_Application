import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token
)
from datetime import datetime, date
from celery_config import celery_init_app
from extensions import mail, cache

# IMPORT API BLUEPRINT
from routes import api_bp
app = Flask(__name__)

# CONFIGURATION
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trekking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your_jwt_secret_key')
app.config["CELERY_BROKER_URL"] = os.environ.get(
    "CELERY_BROKER_URL", "redis://localhost:6379/0"
)
app.config["CELERY_RESULT_BACKEND"] = os.environ.get(
    "CELERY_RESULT_BACKEND", "redis://localhost:6379/0"
)
app.config["CACHE_REDIS_URL"] = os.environ.get(
    "CACHE_REDIS_URL", "redis://localhost:6379/1"
)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get(
    "MAIL_DEFAULT_SENDER", app.config["MAIL_USERNAME"]
)

# INITIALIZE EXTENSIONS
CORS(app)
db.init_app(app)
jwt = JWTManager(app)

mail.init_app(app)
cache.init_app(app)
celery_app = celery_init_app(app)


# REGISTER ALL ROUTES
app.register_blueprint(api_bp)

# USER REGISTRATION
@app.route('/api/register', methods=['POST'])
def register():

    data = request.get_json()

    # Check Email
    if User.query.filter_by(email=data['email']).first():
        return jsonify({
            'success': False,
            'message': 'Email already exists'
        }), 400

    # Check Mobile Number
    if User.query.filter_by(mobile_number=data['mobile_number']).first():
        return jsonify({
            'success': False,
            'message': 'Mobile number already exists'
        }), 400

    user = User(
        full_name=data['full_name'],
        email=data['email'],
        mobile_number=data['mobile_number'],
        password_hash=generate_password_hash(data['password']),
        date_of_birth=datetime.strptime(data['date_of_birth'],"%Y-%m-%d").date(),
        gender=data['gender'],
        city=data['city'],
        state=data['state'],
        emergency_contact_name=data['emergency_contact_name'],
        emergency_contact_number=data['emergency_contact_number'],
        role='user',
        status='Active'
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'User Registered Successfully'
    }), 201


# ==========================================================
# LOGIN (USER / STAFF / ADMIN)
# ==========================================================

@app.route('/api/login', methods=['POST'])
def login():

    data = request.get_json()

    email = data.get('email')
    password = data.get('password')
    selected_role = data.get('role')

    # ==========================
    # Validate Input
    # ==========================

    if not email or not password or not selected_role:

        return jsonify({
            'success': False,
            'message': 'Email, Password and Role are required.'
        }), 400

    # ==========================
    # Find User
    # ==========================

    user = User.query.filter_by(email=email).first()

    if not user:

        return jsonify({
            'success': False,
            'message': 'Invalid Email or Password.'
        }), 401

    # ==========================
    # Check Password
    # ==========================

    if not check_password_hash(
        user.password_hash,
        password
    ):

        return jsonify({
            'success': False,
            'message': 'Invalid Email or Password.'
        }), 401

    # ==========================
    # Check Account Status
    # ==========================

    if user.status != "Active":

        return jsonify({
            'success': False,
            'message': 'Your account has been deactivated. Please contact the administrator.'
        }), 403

    # ==========================
    # Check Selected Role
    # ==========================

    if user.role.lower() != selected_role.lower():

        return jsonify({
            'success': False,
            'message': f'This account is registered as {user.role.capitalize()}. Please select the correct role.'
        }), 403

    # ==========================
    # Update Last Login
    # ==========================

    user.last_login = datetime.utcnow()

    db.session.commit()

    # ==========================
    # Generate JWT
    # ==========================

    access_token = create_access_token(
        identity=str(user.id)
    )

    # ==========================
    # Success Response
    # ==========================

    return jsonify({

        'success': True,

        'message': 'Login Successful',

        'data': {

            'id': user.id,

            'full_name': user.full_name,

            'email': user.email,

            'role': user.role,

            'profile_picture': user.profile_picture,

            'access_token': access_token

        }

    }), 200



# ==========================================================
# HOME ROUTE
# ==========================================================

@app.route('/', methods=['GET'])
def home():

    return jsonify({
        'application': 'Trekking Management System',
        'version': '1.0',
        'status': 'Backend Running Successfully'
    })



# ==========================================================
# RUN APPLICATION
# ==========================================================

if __name__ == '__main__':

    with app.app_context():

        db.create_all()

        if not User.query.filter_by(
            email='admin@trekmate.com'
        ).first():

            admin = User(
                full_name='Administrator',
                email='admin@trekmate.com',
                mobile_number='9999999999',
                password_hash=generate_password_hash('Admin@123'),
                date_of_birth=date(2000, 1, 1),
                gender='Male',
                city='Delhi',
                state='Delhi',
                emergency_contact_name='Administrator',
                emergency_contact_number='9999999999',
                role='admin',
                status='Active'
            )

            db.session.add(admin)
            db.session.commit()

    app.run(debug=True)
