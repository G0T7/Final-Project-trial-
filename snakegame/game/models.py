# game/models.py

from django.db import models

class GameScore(models.Model):
    player_name = models.CharField(max_length=100)  # New field
    score = models.IntegerField()

    def __str__(self):
        return f"{self.player_name} - {self.score}"

