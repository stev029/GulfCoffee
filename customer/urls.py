from django.urls import path, include
from customer import views

# Used a mixture of url patters. path() comes from the DjangoRestFramework
# and url() is out of the box Django code.
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('customer/superusers/',
         views.SuperuserList.as_view(), name='superuser-list'),
    path('customer/staff/', views.StaffList.as_view(), name='staff-list'),
    path('address/<uuid:pk>', views.AddressViews.as_view(), name='address'),
]
