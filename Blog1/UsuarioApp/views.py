from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
           # messages.success(request, 'La cuenta ha sido creada con éxito.')
            return redirect('Post')  # Redirigir a la página de inicio después del registro
    else:
        form = UserRegisterForm()
    return render(request,'UsuarioApp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Post')  # Redirigir a la página de inicio después del inicio de sesión
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
                return redirect('Register')
    else:
        form = UserLoginForm()
    return render(request, 'UsuarioApp/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('Inicio')