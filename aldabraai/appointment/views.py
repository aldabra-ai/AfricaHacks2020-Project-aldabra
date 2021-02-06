from .models import Appointment
from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404



## Send Email Notification To Doctor on Appointment Request
def notify_doctor(request, pk):
    ## get appointment and doctors email, well you should know that
    appointment = get_object_or_404(Appointment, pk=pk)
    email_address = appointment.get_doctor_email
    sender = 'amidbidee@gmail.com'

    ## appointment detail url
    appointment_url = appointment.get_absolute_url
    
    subject, from_email, to = "Appointment Request", f'{sender}', f'{email_address}'
    text_content = "Someone Requested an Appointment with you, please review it here"
    html_content = f"<p>Someone Requested an Appointment with you, please review it <a href='{appointment_url}'>here</a></p>"
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    ## redirect to homepage(for now)
    return redirect('home')