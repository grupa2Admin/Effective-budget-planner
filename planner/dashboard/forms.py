from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


# class RegisterForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class UpdateProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]



class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username.."}),
            "email": forms.Textarea(attrs={"placeholder": "email@org.com"}),
            "password1": forms.Textarea(attrs={'placeholder': 'Enter password...'}),
            "password2": forms.Textarea(attrs={'placeholder': 'Re-enter Password...'}),
        }
