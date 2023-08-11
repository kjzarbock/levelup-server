from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    date = models.DateField()
    location = models.CharField(max_length=255)