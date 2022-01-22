from celery import shared_task

from django.core.mail import send_mail , EmailMessage
from config.settings import EMAIL_HOST_USER


@shared_task(bind=True)
def send_mail_task(request,subject, message, to_email, from_email = EMAIL_HOST_USER):
    send_mail(
        subject = subject,
        message=message,
        from_email=from_email,
        recipient_list=to_email,
        fail_silently=False,
    )
    return 'Done'

@shared_task(bind=True)
def send_mail_from_webmaster_task(request,subject, message, to_email):
    email = EmailMessage(subject, message, to=to_email)
    email.send()
    return 'Done'