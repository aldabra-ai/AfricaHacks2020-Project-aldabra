from django.shortcuts import render, redirect

def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'hospitaldb/dashbaord')

# Create your views here.
