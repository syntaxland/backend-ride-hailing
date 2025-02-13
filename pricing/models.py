from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 


class RideRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ride_user')
    distance_km = models.FloatField()
    traffic_level = models.CharField(max_length=10, choices=[('low', 'Low'), ('normal', 'Normal'), ('high', 'High')])
    demand_level = models.CharField(max_length=10, choices=[('low', 'Low'), ('normal', 'Normal'), ('peak', 'Peak')])
    calculated_fare = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride {self.id} - {self.calculated_fare}$"
    