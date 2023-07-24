from django.urls import path

from cart import views

urlpatterns = [
    path('cart/', views.CartViews.as_view(), name='cart-list'),
    path('cart/<uuid:pk>/', views.CartUpdateViews.as_view(), name='cart-detail'),
]
