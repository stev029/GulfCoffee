from rest_framework.fields import MaxValueValidator

from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    REQUIRED_FIELDS = ['username', 'first_name',
                       'last_name', 'is_superuser', 'is_staff']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


class AddressCustomer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=100)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, blank=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    region = models.CharField(max_length=50)
    user = models.ForeignKey(
        'customer.User', on_delete=models.CASCADE, related_name='address')

    def __str__(self):
        return self.title
