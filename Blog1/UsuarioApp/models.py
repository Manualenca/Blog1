from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    apodo = models.TextField()

    def __str__(self):
        return self.username