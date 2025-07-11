from django import forms
from accounts.models import CustomUser
from diary import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            "class":"bg-stone-100 px-4 py-2 outline-none rounded-md w-full",
            "placeholder": "Sua senha"
        })
    )
    
    password2 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            "class":"bg-stone-100 px-4 py-2 outline-none rounded-md w-full",
            "placeholder": "Sua senha"
        })
    )
    
    class Meta:
        model = CustomUser
        fields = ['email', 'myname', 'birthday']
        widgets = {
            'myname': forms.TextInput(attrs={"class": "bg-stone-100 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Type your name"}),
            'birthday': forms.DateInput(attrs={"class": "bg-stone-100 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Ex: 19/11/2005"}),
            'email': forms.EmailInput(attrs={"class": "bg-stone-100 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Type your email"}),
        }
        
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={"class": "bg-stone-100 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Your email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "bg-stone-100 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Your password"}))