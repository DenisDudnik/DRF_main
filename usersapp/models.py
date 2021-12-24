from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    birthday = models.DateField(null=True, blank=True)
    uuid = models.UUIDField(primary_key=True, default=uuid4())
