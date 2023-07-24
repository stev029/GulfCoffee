from rest_framework import serializers, exceptions

from cart import models
from menu.models import Menu
from utils.serializers import StringPrimaryKeyRelateField


class CartSerializer(serializers.ModelSerializer):
    item = StringPrimaryKeyRelateField(
        queryset=Menu.objects.all())

    class Meta:
        model = models.CartModel
        fields = ("quantity", "note", "item")

    def validate_item(self, value):
        if self.instance and self.instance.item != value:
            raise exceptions.ValidationError("You may not edit this field.")
        return value
