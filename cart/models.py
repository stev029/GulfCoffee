from rest_framework.fields import MinValueValidator, MaxValueValidator

from django.db import models

import uuid


class CartModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        "customer.User", models.CASCADE, related_name='cart')
    item = models.ForeignKey("menu.Menu", models.CASCADE)
    quantity = models.IntegerField(
        default=1, validators=[MinValueValidator(1)])
    note = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.item.name
