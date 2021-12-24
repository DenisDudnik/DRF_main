from django.db import models
from uuid import uuid4

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=64, blank=False)
    email = models.EmailField(unique=True, max_length=128, blank=False)
    password = models.CharField(max_length=64, blank=False)
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    birthday = models.DateField(blank=True)
    uuid = models.UUIDField(primary_key=True, default=uuid4())
