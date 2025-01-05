from celery import shared_task
from django.core.mail import send_mail



@shared_task(name="task_send_email")
def task_send_email(email_from, full_name, phone, email, note, date_arrival, date_departure):    
    subject = 'Nová zpráva z webu Prachovec'
    message = 'Jméno: ' + full_name + '\n' + 'Telefon: ' + phone + '\n' + 'Email: ' + email + '\n' + 'Poznámka: ' + note + '\n' + 'Datum příjezdu: ' + str(date_arrival) + '\n' + 'Datum odjezdu: ' + str(date_departure)
    email_from = email_from
    recipient_list = ['synek.o@seznam.cz', 'synekjbc@gmail.com', 'synek.o@seznam.cz',]   
    send_mail( subject, message, email_from, recipient_list )  
    return f"Sent email to {len(recipient_list)} recipients."