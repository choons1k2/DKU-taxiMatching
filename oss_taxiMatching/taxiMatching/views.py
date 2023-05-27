#로그인

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})




#로그인 시 home 화면 - 합승 리스트 조회로 참여 및 생성 가능




def home(request):
    matching_list = Matching.objects.all()
    return render(request, 'home.html', {'matching_list': matching_list})



from .models import Matching
from .forms import MatchingForm

def create_matching(request):
    if request.method == 'POST':
        form = MatchingForm(request.POST)
        if form.is_valid():
            matching = form.save(commit=False)
            matching.driver = request.user
            matching.save()
            return redirect('matching_detail', matching_id=matching.id)
    else:
        form = MatchingForm()
    return render(request, 'create_matching.html', {'form': form})



from django.shortcuts import get_object_or_404


def matching_list(request):
    matching_list = Matching.objects.all()
    return render(request, 'matching_list.html', {'matching_list': matching_list})

def matching_detail(request, matching_id):
    matching = get_object_or_404(Matching, id=matching_id)
    return render(request, 'matching_detail.html', {'matching': matching})
