from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from .models import User, AddressCustomer
from cart.serializers import CartSerializer

# Create your serializers here


class UserCreateSerializer(UserCreateSerializer):
    cart = CartSerializer(many=True, read_only=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'password', 'first_name',
                  'last_name', 'is_superuser', 'is_staff', 'cart']
        depth = 2


class CurrentUserSerializer(UserSerializer):
    cart = CartSerializer(many=True, read_only=True)

    class Meta(UserSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'first_name',
                  'last_name', 'is_superuser', 'is_staff', 'cart', 'address']
        depth = 2


class AddressSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = AddressCustomer
        fields = '__all__'
