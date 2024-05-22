from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password1', 
            'password2',
        ]            

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = [
            'profile_picture',
            'about',
        ]
        
