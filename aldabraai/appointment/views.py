from django.http.response import Http404
from .models import Appointment
from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404

## default Mail list
Mail_List = {
    'sender': 'amidbidee@gmail.com',
}

def sendEmailNotification(subject, email_address, sender, html_con, text_con=None):
    html_content = html_con
    text_content = text_con
    msg = EmailMultiAlternatives(subject, html_content, sender, [email_address])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

## Send Email Notification To Doctor on Appointment Request
def notifyDoctor(request, pk):
    ## get appointment and doctors email, well you should know that
    appointment = get_object_or_404(Appointment, pk=pk)
    email_address = appointment.get_doctor_email

    ## appointment detail url
    appointment_url = appointment.get_absolute_url()

    ## THIS IS FOR DEVELOPMENT PURPOSE USING DJANGO SMTP MAIL TOOL
    Mail_List = {
        'subject': 'Appointment Request',
        'email_address': email_address,

        'text': "Someone Requested an Appointment with you, please review it here",
        'html': f"<p>Someone Requested an Appointment with you, please review it <a href='{appointment_url}'>here</a></p>",
        'sender': 'amidbidee@gmail.com'
    }

    sendEmailNotification(
        Mail_List['subject'], 
        Mail_List['email_address'], 
        Mail_List['sender'], 
        Mail_List['html'])
    
    ## redirect to homepage(for now)
    return redirect('home')


def acceptSetTimer(request, pk):
    ## get appointment
    appointment = get_object_or_404(Appointment, pk=pk)

    if appointment:
       try:
           if appointment.appointment_state == 'AC':
               pass
           else:
               appointment.setState('AC') ## set appointment state AC:Accepted
               appointment.save()

           date = appointment.appointment_date
           time = appointment.appointment_time

           ## THIS IS FOR DEVELOPMENT PURPOSE USING DJANGO SMTP MAIL TOOL
           Mail_List = {
               'doctor_email': appointment.get_doctor_email,
               'patient_email': appointment.get_patient_email,

               'subject1': "Appointment has  been set to",
               'subject2': "Appointment Booked and Accepted",

               'text1': f"""
                                 An Appointment as been set for 
                                 date:'{date}', 
                                 time:'{time}'
                        """,
               'html1': f"""
                                 <p>
                                 An Appointment as been set for;
                                 date:'{date}', 
                                 time:'{time}'
                                 </p>
                        """,

               'text2': f"""
                                 Your Appointment has been accepted and successfully booked.
                                 Appointment as been set for;
                                 date:'{date}', 
                                 time:'{time}'
                        """,
               'html2': f"""
                                 <p>
                                 Your Appointment has been accepted and successfully booked.
                                 Appointment as been set for;
                                 date:'{date}', 
                                 time:'{time}'
                                 </p>
                        """,
           }

           sendEmailNotification(
               Mail_List['subject1'], 
               Mail_List['doctor_email'], 
               Mail_List['sender'], 
               Mail_List['html1'])
           sendEmailNotification(
               Mail_List['subject2'], 
               Mail_List['patient_email'], 
               Mail_List['sender'], 
               Mail_List['html2'])
           
       except appointment.DoesNotExist:
           return Http404

    return redirect('home')


def declineDelete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    
    if appointment:
        try:
            if appointment.appointment_state == 'DE':
                pass
            else: 
                appointment.setState('DE') ## DE:Decline
                appointment.save()

            ## THIS IS FOR DEVELOPMENT PURPOSE USING DJANGO SMTP MAIL TOOL
            Mail_List = {
                'patient_email': appointment.get_patient_email,
                'subject': 'Appointment Declined',

                'text': f"""
                             Your Requested Appointment was declined,
                             the following reasons were provided; {appointment.doctor_dec_reason}
                        """,
                        
                'html': f"""
                            <p>
                             Your Requested Appointment was declined,
                             the following reasons were provided; {appointment.doctor_dec_reason}
                            </p>
                        """
        }

        except appointment.DoesNotExist:
            return Http404

    return redirect('home')


