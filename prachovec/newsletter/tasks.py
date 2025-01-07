from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings



@shared_task(name="task_send_newsletter")
def task_send_newsletter(subject, message, recipients):    
    subject = 'Pravidelný Newsletter z Prachovce'
    send_mail(
        subject=subject, 
        message="",
        html_message=message, 
        from_email=settings.EMAIL_HOST_USER, 
        recipient_list=recipients
        )  
    
    return f"Newsletter {subject} to {len(recipients)} recipients was sent."