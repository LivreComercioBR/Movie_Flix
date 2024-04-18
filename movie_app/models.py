from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser, UserManager):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=264)
    password = models.CharField(max_length=264)

    def __str__(self):
        return self.username
