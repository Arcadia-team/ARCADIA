from django.db import models
from django.contrib.auth.models import User
from app_games.models import Game, Score


class Avatar(models.Model):
    ruta_imagen = models.CharField(max_length=100)
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, default=1)
    bio = models.TextField(max_length=500, blank=True)
    website = models.URLField(max_length=100, blank=True)
    scores = models.ManyToManyField(Game, through=Score, related_name='user_profiles')

    def __str__(self):
        return self.user.username


