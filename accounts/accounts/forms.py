from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "profile_picture",
            "about"
        )

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields + (
            "profile_picture",
            "about"
        )
