from django.contrib import admin
from .models import CategoriesMenu, ImageMenu, Menu, RatingMenu

# Register your models here.

admin.site.register(CategoriesMenu)
admin.site.register(RatingMenu)
admin.site.register(Menu)
admin.site.register(ImageMenu)
