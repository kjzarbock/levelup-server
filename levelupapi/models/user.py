from django.db import models

class User(models.Model):
    gamer = models.OneToOneField("Gamer", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()