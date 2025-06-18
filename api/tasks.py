from celery import shared_task
from django.core.mail import send_mail
import logging
logger = logging.getLogger(__name__)
@shared_task
def send_welcome_email(user_email):
    logger.info(f"📧 Sending welcome email to {user_email}")
    send_mail(
        subject="Welcome to MySite!",
        message="Thanks for registering.",
        from_email="no-reply@mysite.com",
        recipient_list=[user_email],
        fail_silently=False,
    )
    print(f"Welcome email sent to {user_email}")
