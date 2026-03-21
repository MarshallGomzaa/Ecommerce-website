from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . models import User
from .forms import RegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def user_registration(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            # If the form is invalid, Django will automatically handle field errors
            messages.success(request, "Please correct the errors below.")
            return redirect('register')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username = username,
            password = password

        )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password!!')
            return redirect('login')
            

    return render(request,'login.html',{})


def user_logout(request):
    logout(request)
    return redirect('home')


def user_profile(request):
    return render(request,'user_profile.html')


def update_user(request):
    return render(request,'update_user.html')


