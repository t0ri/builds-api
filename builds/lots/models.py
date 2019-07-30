from django.db import models
from django.contrib.auth.models import User

class Lot(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True)

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=000000,
    )
    created_at = models.DateTimeField(auto_now_add=True)