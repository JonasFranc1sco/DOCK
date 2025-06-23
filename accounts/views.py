from django.shortcuts import render, redirect
from accounts.forms import CustomUserForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate, logout

def account_register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('success')
    else:
        form = CustomUserForm()
    return render(request, 'accounts/register.html', {'form': form})

def account_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('success')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def success(request):
    return render(request, 'accounts/success.html')