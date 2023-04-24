from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100)
    numPartidas = models.IntegerField(default=0)

    def __str__(self):
        return self.name



    

class Score(models.Model):
    user_profile = models.ForeignKey('app_perfiles.UserProfile', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_played = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.game.name}: {self.score}"