from celery import Celery
from celery.schedules import crontab


def celery_init_app(app):

    celery = Celery(
        app.import_name,
        broker=app.config["CELERY_BROKER_URL"],
        backend=app.config["CELERY_RESULT_BACKEND"],
        include=["tasks"]
    )

    celery.conf.update(
        timezone="Asia/Kolkata",
        enable_utc=False,
        task_track_started=True,
        result_expires=3600,
        beat_schedule={
            "send-daily-trek-reminders": {
                "task": "tasks.daily_reminder",
                "schedule": crontab(hour=8, minute=0), 
            },
            "send-monthly-activity-report": {
                "task": "tasks.monthly_report",
                "schedule": crontab(hour=8, minute=30, day_of_month=1),
            },
        },
    )

    class FlaskTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = FlaskTask
    celery.set_default()

    app.extensions["celery"] = celery

    return celery
