# common
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login
)

from django.contrib.auth.decorators import (
    login_required
)

# custom utils fuctions
from ..utils import (
    generate_random_string,
    generate_uuid
)


# form class
from ..forms import UserRegistrationForm

# User class
from ..models import User


def registrationView(request):
    """

    """
    context = {

    }

    if request.POST:
        register_form = UserRegistrationForm(request.POST)
        
        if register_form.is_valid():
            register_form.save() 

            data = {
                'email': register_form.cleaned_data['email'],
                'raw_password': register_form.cleaned_data['password1']
            }

            user = User.objects.get(email=data['email'])
            user.user_id =  generate_uuid(use_host=True, use_id=True, use_time=True, rand=False)
            if user.profile_type == 'DR':
                user.is_doctor = True
            elif user.profile_type == 'PT':
                user.is_patient = True
            user.save()

            user = authenticate(email=data['email'], password=data['raw_password'])
            login(request, user)
            messages.success(request, "Hold On Tight")
            return redirect('frontend:dashboard')
    
        else:
            messages.error(request, "Please Correct Errors")
            context['register_form'] = register_form
    
    else:
        register_form = UserRegistrationForm()
        context['register_form'] = register_form
    
    return render(request, 'authend/registration.html', context)


@login_required()
def onboardingPath(request):
    user = request.user
    if user.is_patient:
        return redirect('patient_onboarding')
    elif user.is_doctor:
        return redirect('doctor_onboarding')