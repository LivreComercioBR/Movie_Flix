from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from filme_app.models import Filme


class User(AbstractUser, UserManager):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=264)
    password = models.CharField(max_length=264)
    filmes_vistos = models.ManyToManyField(
        Filme, related_name='filmes', blank=True)

    def __str__(self):
        return self.username
