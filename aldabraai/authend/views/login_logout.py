# django common
from django.contrib.auth import (
    authenticate, 
    login, 
    logout
)
from django.http import response
from django.shortcuts import (
    render, 
    redirect
)

from django.http import (
    HttpResponse,
    HttpResponseRedirect
)

# form class
from ..forms import LoginForm

# requests
import requests

from django.contrib import messages



def userLoginView(request):
    """
    """

    # first check if user id logged in, if true redirect home
    user = request.user
    if user.is_authenticated:
        return redirect('frontend:dashboard')

    if request.POST:
        login_form = LoginForm(request.POST)
        
        data = {
                'email': request.POST.get('email'),
                'password': request.POST.get('password')
            }

        user = authenticate(email=data['email'], password=data['password'])

        if user is not None:
            login(request, user)
            return redirect('frontend:dashboard')
        else:
            messages.error(request,"Email or Password Incorrect")

    else:
        login_form = LoginForm()

    return render(request, 'authend/login.html', {
        'login_form': login_form
    })


def logout_view(request):
    logout(request)
    return redirect('/auth/login/')

