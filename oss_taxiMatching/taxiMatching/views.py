#로그인


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # 로그인 후 이동할 페이지를 지정합니다.
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#회원가입

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

