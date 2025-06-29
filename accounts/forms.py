from django import forms
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'myname', 'birthday', 'password1', 'password2']
        widgets = {
            'myname': forms.TextInput(attrs={"class": "bg-gray-700 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Type your name"}),
            'birthday': forms.DateInput(attrs={"class": "bg-gray-700 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Ex: 19/11/2005"}),
            'email': forms.EmailInput(attrs={"class": "bg-gray-700 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Type your email"}),
            'password1': forms.PasswordInput(attrs={"class": "bg-gray-700 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Type your password"}),
            'password2': forms.PasswordInput(attrs={"class": "bg-gray-700 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Confirm your password"})
        }
        
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={"class": "bg-gray-700 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Your email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "bg-gray-700 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Your password"}))