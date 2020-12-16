from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import json
from patient.models import Patient

@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.filter(provider='auth0')
    # userdata = {
    #      'user_id': auth0user.uid,
    #      'name': user.first_name,
    #      'picture': auth0user.extra_data['picture'],
    #      'email': auth0user.extra_data['email'],
    #  }

    # if Patient.objects.get(user=user) is True:
    #      pass
    #  else:
    #      Patient.objects.create(user=user) 
    patient_profile = Patient.objects.get_or_create(user=user)

    return render(request, 'dashboard/dashboard.html', {
        'auth0User': auth0user,
        'patient': patient_profile,
        #'userdata': json.dumps(userdata, indent=4)
    })


