from django.db import models
from django.contrib.auth.models import User

class RideShare(models.Model):
    title = models.CharField(max_length=200)
    departure_location = models.CharField(max_length=200)
    destination_location = models.CharField(max_length=200)
    departure_time = models.DateTimeField()
    max_passengers = models.IntegerField()
    passengers = models.ManyToManyField(User, related_name="ride_shares", blank=True)





