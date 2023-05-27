from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RideShare
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})





class RideShareDetailView(DetailView):
    model = RideShare
    template_name = 'ride_share_detail.html'

    def post(self, request, *args, **kwargs):
        ride_share = get_object_or_404(RideShare, pk=kwargs['pk'])
        ride_share.passengers.add(request.user)
        ride_share.save()
        return HttpResponseRedirect(reverse('ride_share_detail', args=[ride_share.id]))

class RideShareDetailView(DetailView):
    model = RideShare
    template_name = 'ride_share_detail.html'

class RideShareCreateView(LoginRequiredMixin, CreateView):
    model = RideShare
    template_name = 'ride_share_form.html'
    fields = ['title', 'departure_location', 'destination_location', 'departure_time', 'max_passengers']







