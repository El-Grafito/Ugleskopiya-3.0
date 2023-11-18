from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username = cd['username'],
                password = cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main')
                else:
                    messages.error(request, 'Аккаунт не активен')
            else:
                messages.error(request, 'Неверные данные')
        else:
            messages.error(request, 'Ошибка в заполнении полей')
    else:
        form = LoginForm()
    context = {'form': form,}
    return render(request, 'login.html', context)

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            confirm_password = cd['confirm_password']            
            try:
                if password == confirm_password:
                    user = User.objects.create_user(username=username, password=confirm_password)
                    login(request, user)
                    return redirect('edit_profil')
                else:
                    messages.error(request, 'Ошибка в заполнении паролей')
            except IntegrityError:
                messages.error(request, 'Это имя пользователя уже занято. Пожалуйста, выберите другое')
        else:
            messages.error(request, 'Ошибка в заполнении полей')
    else:
        form = SignupForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def logout_cheta(request):
    logout(request)
    # return redirect('main')
    return render(request, 'logout.html') #Не забудь закомментировать это и разкомментировать строку выше
