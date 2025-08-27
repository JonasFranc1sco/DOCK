from django import forms
from PIL import Image
from accounts.models import CustomUser
from diary import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class":"bg-stone-100 px-4 py-2 outline-none rounded-md w-full",
            "placeholder": "Your password"
        })
    )
    
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={
            "class":"bg-stone-100 px-4 py-2 outline-none rounded-md w-full",
            "placeholder": "Confirm your password"
        })
    )

    birthday = forms.DateField(
        required=True,
        widget=forms.DateInput(
                 attrs={
                "type": "date",
                "class": "bg-stone-100 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Month/Day/Year"
                })
    )
    avatar = forms.ImageField(
            required=False,
            widget=forms.ClearableFileInput(attrs={"class": "bg-stone-100 px-4 py-2 outline-none rounded-md w-full"})
        )
    
    class Meta:
        model = CustomUser
        fields = ['email', 'real_name', 'user_name', 'birthday', 'avatar']
        widgets = {
            'real_name': forms.TextInput(attrs={"class": "bg-stone-100 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Type your real name"}),
            'user_name': forms.TextInput(attrs={"class": "bg-stone-100 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Type your username"}),
            'email': forms.EmailInput(attrs={"class": "bg-stone-100 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Type your email"}),
        }
        
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={"class": "bg-stone-100 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Your email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "bg-stone-100 px-4 py-2 outline-none rounded-md w-full", "placeholder": "Your password"}))

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['real_name', 'user_name', 'avatar']
        widgets = {
            'real_name': forms.TextInput(attrs={"class": "bg-zinc-800 text-white px-4 py-2 rounded-md w-full", "placeholder": "Name"}),
            'user_name': forms.TextInput(attrs={"class": "bg-zinc-800 text-white px-4 py-2 rounded-md w-full", "placeholder": "User"}),
            'avatar': forms.ClearableFileInput(attrs={"class": "bg-gray-700 text-white"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].widget.clear_checkbox_label = ''

