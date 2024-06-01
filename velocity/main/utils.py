from django.core.mail import send_mail

def send_my_email(subject, message, from_email, recipient_list):
    return send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
    )