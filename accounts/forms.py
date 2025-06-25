from django import forms
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['myname', 'birthday', 'email', 'password1', 'password2']
        
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)