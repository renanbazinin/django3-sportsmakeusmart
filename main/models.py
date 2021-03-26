from django.db import models


class MindGames(models.Model):
    title = models.CharField(max_length=100)
    textlist = models.TextField()
    

    def __str__(self):
        return self.textlist

class MindGameswins(models.Model):
    title = models.CharField(max_length=105)
    wons = models.TextField()
    

    def __str__(self):
        return self.wons

# Create your models here.
