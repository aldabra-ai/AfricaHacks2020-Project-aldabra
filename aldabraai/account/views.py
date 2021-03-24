from .models import Patient
from django.shortcuts import redirect, get_object_or_404



def setProfileSlug(request):
    profile = get_object_or_404(Patient, owner=request.user)
    username = request.user.identifier
    profile.set_slug_as_username(username)
    profile.save()
    return redirect('home')
