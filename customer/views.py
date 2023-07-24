from .models import User, AddressCustomer
from .serializers import CartSerializer, UserCreateSerializer, AddressSerializer

from rest_framework import generics, permissions

# Create your views here.


class SuperuserList(generics.ListCreateAPIView):
    queryset = User.objects.filter(is_superuser=True)
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StaffList(generics.ListCreateAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AddressViews(generics.UpdateAPIView,
                   generics.DestroyAPIView,
                   generics.CreateAPIView):
    queryset = AddressCustomer.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
