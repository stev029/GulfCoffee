from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root),
    path('menu/', views.MenuList.as_view(), name='menu-list'),
    path('menu/<uuid:pk>/', views.MenuDetail.as_view(), name='menu-detail'),
    path('category/<str:name>/', views.CategoryDetail.as_view(),
         name='categoriesmenu-detail'),
]
