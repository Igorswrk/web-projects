from django.db import models
from django.contrib.auth.models import AbstractUser 

class CustomUser(AbstractUser): 
    date_enroll_at = models.DateTimeField(auto_now_add=True)
    date_update_at = models.DateTimeField(auto_now=True)
    amount_reviews = models.PositiveIntegerField(default=0)
    profile_picture = models.ImageField(blank=True)
    about = models.TextField(editable=True, max_length=255, blank=True)

    def __str__(self):
        return self.username

    def _get_reviews(self):
        pass