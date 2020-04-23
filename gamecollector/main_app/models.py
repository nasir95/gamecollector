from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Console(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"A {self.color} {self.name}"


class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.CharField(max_length=2)
    description = models.TextField(max_length=250)
    date = models.DateField('Released Year')
    consoles = models.ManyToManyField(Console)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})
