from django.shortcuts import render, redirect
from accounts.models import CustomUser
from accounts.forms import CustomUserForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate, logout

def account_register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_feed')
    else:
        form = CustomUserForm()
    return render(request, 'accounts/register.html', {'form': form})

def account_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('post_feed')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def success(request):
    return render(request, 'accounts/success.html')

def home(request):
    return render(request, 'accounts/home.html')

def account_edit(request, user_id):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(pk=user_id)
        if request.method == 'POST':
            form = CustomUserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('user_post')
        else:
            form = CustomUserForm(instance=user)
            
        return render(request, 'accounts/account_edit.html', {'form': form})
    
def account_delete(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    user.delete()
    redirect('register')