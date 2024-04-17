from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

# Create your views here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

def home_view(request):
    return render(request, "home.html")

def user_signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def user_profile_view(request, id):
    try:
        user = CustomUser.objects.get(id=id)
    except CustomUser.DoesNotExist:
        return HttpResponse("user not found!")
    return render(request, "user_profile.html", {'user': user})

def user_list_view(request):
    users = CustomUser.objects.all()
    return render(request, "user_list.html", {'users': users})

def user_delete_view(request, id):
    if request.method == "POST": 
        user = CustomUser.objects.get(id=id)
        user.delete()
        return redirect('home') 
        
    return render(request, "user_delete.html")

def user_update_view(request, id):
    user = CustomUser.objects.get(id=id)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', user.id)
    else:
        form = CustomUserChangeForm(instance=user)
    
    return render(request, 'user_update.html', {'form': form})