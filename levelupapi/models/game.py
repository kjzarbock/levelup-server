from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="created_games")
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name="games")