from django.db import models

class EventGamer(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="participants")
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="attended_events")