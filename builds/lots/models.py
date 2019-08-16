from django.db import models
from django.contrib.auth.models import User

class Lot(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True)
    gallery = models.CharField(max_length=1000, blank=True)
    
    lot_type = models.CharField(max_length=100, default='undefined')
    bedrooms = models.CharField(max_length=3, blank=True)
    bathrooms = models.CharField(max_length=3, blank=True)
    sims = models.CharField(max_length=3, blank=True)

    images = models.TextField(default='undefined')

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=000000,
    )
    created_at = models.DateTimeField(auto_now_add=True)