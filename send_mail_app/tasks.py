from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

@shared_task
def send_mail_func():
    users = get_user_model().objects.exclude(email="")

    for user in users:
        mail_subject = "Hi! Celery Testing"

        message = (
            "If you are liking my content, "
            "please hit the like button and connect to my page."
        )

        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )

    return "Done"