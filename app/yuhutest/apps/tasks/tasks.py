from django.core.mail import send_mail
from celery import shared_task
statuses = {"created": "New Task", "updated": "Task Updated"}


@shared_task
def task_email_notification(email, title, due_date, description, status, email_host_user):
    message = f'{statuses[status]}: {title}\n\n{description}\n\nDue Date: {due_date}'
    try:
        send_mail(
            subject=status,
            message=message,
            from_email=email_host_user,
            recipient_list=[email]
        )
    except Exception as e:
        print(e)
        raise e

