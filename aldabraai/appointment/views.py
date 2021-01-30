from django.shortcuts import render
from .models import Appointment
from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404



def notify_doctor(self, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    email_address = appointment.booked_doctor_office.office_onwer.email
    sender = 'amidbidee@gmail.com'

    appointment_url = appointment.get_absolute_url
    
    subject, from_email, to = "Appointment Request", f'{sender}', f'{email_address}'
    text_content = "Someone Requested an Appointment with you, please review it here"
    html_content = f'<p>Someone Requested an Appointment with you, please review it <a href={appointment_url}>here</a></p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return redirect('home')