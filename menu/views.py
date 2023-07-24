from menu.serializers import *
from menu.models import *
from utils.filters import QueryParamsFilter

from rest_framework import generics, permissions, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'superusers': reverse('superuser-list', request=request, format=format),
        'staff': reverse('staff-list', request=request, format=format),
        'menu': reverse('menu-list', request=request, format=format),
    })


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriesMenu.objects.all()
    serializer_class = CategoriesDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'name'


class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RatingAdd(generics.CreateAPIView):
    serializer_class = RatingSerializers
    permission_classes = [permissions.IsAuthenticated]
