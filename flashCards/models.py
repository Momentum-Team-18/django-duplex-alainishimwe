from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)


class Deck(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
    
class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question

