from rest_framework import generics, permissions
from rest_framework.views import Response

from cart import serializers, models
from utils.permissions import IsOwner


class CartViews(generics.ListCreateAPIView):
    queryset = models.CartModel.objects.all()
    serializer_class = serializers.CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(user=request.user)
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartUpdateViews(generics.UpdateAPIView,
                      generics.DestroyAPIView):
    queryset = models.CartModel.objects.all()
    serializer_class = serializers.CartSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
