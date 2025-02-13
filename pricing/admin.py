# user_profile/admin.py
from django.contrib import admin
from . import models


@admin.register(models.RideRequest)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('distance_km',  
                    'traffic_level', 
                    'demand_level',  
                    'calculated_fare',  
                    'timestamp',  
                    )
    