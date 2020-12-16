from django.shortcuts import render, redirect
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
from patient.models import Patient


# primary login view
def login_view(request):
    user = request.user
    if user.is_authenticated:
        #created =  Patient.objects.get_or_create(user=user)    # creates a patient profile if not found
        return redirect('dashboard')
    else:
        return render(request, 'dashboard/dashbaord.html')

# Create your views here.



def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return redirect(logout_url)