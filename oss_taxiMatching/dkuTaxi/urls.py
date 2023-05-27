
from django.urls import path
from .views import signup_view, login_view

app_name = 'dkuTaxi'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    # 나머지 URL 설정
]
