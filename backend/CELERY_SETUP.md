# Redis and Celery setup

Install the additional job dependencies (the existing `requirements.txt` is UTF-16 encoded, so these are listed here rather than modifying it):

```powershell
pip install "celery==5.5.3" "redis==6.2.0" "Flask-Mail==0.10.0" "Flask-Caching==2.3.1"
```

Start Redis, then open two terminals in `backend`:

```powershell
python -m celery -A celery_worker worker --pool=solo --loglevel=info
python -m celery -A celery_worker beat --loglevel=info
```

Set the variables in `.env.example` in your terminal before starting the app, worker, or Beat. The default Redis broker is database `0`; Flask cache uses database `1`.

Celery Beat runs:

- the next-day trek reminder at 08:00 Asia/Kolkata every day;
- the previous-month activity report at 08:30 Asia/Kolkata on the first day of every month.

On Windows, use `--pool=solo` for the worker. Celery's default prefork pool is designed for Unix-like systems and can fail under Windows process spawning.
