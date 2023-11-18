from django.core.mail import send_mail


def send_message(email, message, status, email_host_user):
    send_mail(
        subject=status,
        message=message,
        from_email=email_host_user,
        recipient_list=[email]
    )