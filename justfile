start-celery:
    celery -A config worker -l info

start:
  python manage.py runserver
