from django.contrib.auth.forms import UserCreationForm
from dkuTaxi.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
