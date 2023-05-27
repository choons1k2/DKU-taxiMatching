# app - urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('create/', views.create_matching, name='create_matching'),
    path('list/', views.matching_list, name='matching_list'),
    path('detail/<int:matching_id>/', views.matching_detail, name='matching_detail'),
]


