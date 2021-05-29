# django generic view classes
from django.views.generic import TemplateView

# models
from appointment.models import Appointment
from authend.models import User

# decorators
from django.contrib.auth.decorators import (
    login_required,
    permission_required
)

# helper/shortcut functions
from django.shortcuts import (
    get_object_or_404,
    render
)


@login_required()
def dashboard(request):
    user = request.user

    template_name = ''
    context = {
        
    }

    if user.is_patient:
        template_name = 'dashboards/patient_dashboard.html'

        context = {
            
        }

    elif user.is_doctor:
        template_name = 'dashboards/doctor_dashboard.html'
        
        context = {

        }
        
    return render(request, template_name, context)

