from django.db import models
from django.contrib.auth.models import User
from app_games.models import Game, Score

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/')

    # Otros campos adicionales para el perfil
    # Ejemplo:
    bio = models.TextField(max_length=500, blank=True)
    website = models.URLField(max_length=100, blank=True)
    scores = models.ManyToManyField(Game, through=Score, related_name='user_profiles')

    def __str__(self):
        return self.user.username