from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserUpdateForm

def login_view(request):
    """Vista de inicio de sesión"""
    if request.user.is_authenticated:
        return redirect('core_p6:home')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido {username}!')
                return redirect('core_p6:home')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'auth_p6/login.html', {'form': form})

def register_view(request):
    """Vista de registro de usuario"""
    if request.user.is_authenticated:
        return redirect('core_p6:home')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada exitosamente para {username}!')
            login(request, user)
            return redirect('core_p6:home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'auth_p6/register.html', {'form': form})

@login_required
def profile_view(request):
    """Vista del perfil de usuario"""
    return render(request, 'auth_p6/profile.html')

@login_required
def profile_edit_view(request):
    """Vista para editar el perfil de usuario"""
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Perfil actualizado exitosamente!')
            return redirect('auth_p6:profile')
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'auth_p6/profile_edit.html', {'form': form})
