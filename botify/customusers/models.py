from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    address = models.TextField()
    date_of_birth = models.DateField()

    USERNAME_FIELD = "email"
