from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

class AuthorPoint(models.Model):
    author = models.OneToOneField(CustomUser, related_name='author_points', on_delete=models.CASCADE)
    point = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.author} - {self.point}"