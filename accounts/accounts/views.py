from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
from .forms import CustomUserCreationForm, CustomUserChangeFrom
from .models import CustomUser

def home_view(request):
    return render(request, "home.html")

def list_view(request):
    users = CustomUser.objects.all()
    context = {'users': users}
    return render(request, "user_list.html", context)

def sign_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login.html")
    else:
        form = CustomUserCreationForm()
        context = {'form': form}
    
    return render(request, 'signup.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("login.html")
    else:
        form = AuthenticationForm()
        context = {'form' : form}

    return render(request, 'signup.html', context)

def logout_view(request):
    logout(request)
    redirect("signup.html")