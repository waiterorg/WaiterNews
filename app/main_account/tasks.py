from celery.utils.log import get_task_logger
from celery import shared_task

from django.core.mail import send_mail


@shared_task(bind=True)
def send_mail_task(self,subject, message, from_email):
    from_email = from_email
    send_mail(
        subject = subject,
        message=message,
        from_email=from_email,
        recipient_list=['iwaiterorg@gmail.com'],
        fail_silently=False,
    )
    return 'Done'