from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email, username):
    send_mail(
        subject='Welcome to TaskTracker!',
        message=f'Hello {username}, thanks for registering.',
        from_email='no-reply@tasktracker.com',
        recipient_list=[email],
        fail_silently=False,
    )
