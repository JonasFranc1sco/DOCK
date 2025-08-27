from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from accounts.forms import CustomUserForm, CustomAuthenticationForm, ProfileEditForm
from django.contrib.auth import login, authenticate, logout
from django.http import FileResponse

# Função para retornar o avatar do usuário
def serve_avatar(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if not user.avatar or not user.avatar.name:
        # Retornar avatar padrão ou erro 404
        return redirect('/static/img/default-avatar.png')
    
    if request.user.is_authenticated and (request.user == user or request.user.is_staff):
        try:
            return FileResponse(open(user.avatar.path, 'rb'), as_attachment=False)
        except FileNotFoundError:
            return redirect('/static/img/default-avatar.png')
    else:
        return redirect('login')

# Função para registrar usuários
def account_register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = CustomUserForm()
    return render(request, 'accounts/register.html', {'form': form})

# Função de log in
def account_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('feed')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Função log out dos usuários
def account_logout(request):
    logout(request)
    return redirect('home')

def success(request):
    return render(request, 'accounts/success.html')

def home(request):
    return render(request, 'accounts/home.html')

# Função para o usuário editar o próprio perfil
def account_edit(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = get_object_or_404(CustomUser, pk=user_id)

    if request.user != user:
        return redirect('feed')
    
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('feed')
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = ProfileEditForm(instance=user)
        
    return render(request, 'accounts/account_edit.html', {'form': form})
    
# Função para deletar a própria conta
def account_delete(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = get_object_or_404(CustomUser, pk=user_id)
    
    if request.user != user:
        return redirect('feed')
    
    if request.method == 'POST':
        user.delete()
        return redirect('register')

    return render(request, 'accounts/delete_confirm.html', {'user': user})