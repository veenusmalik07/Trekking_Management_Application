from app import app as flask_app

celery = flask_app.extensions["celery"]
