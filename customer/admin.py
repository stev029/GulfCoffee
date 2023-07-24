from django.contrib import admin
from .models import User, AddressCustomer
from cart.models import CartModel as Cart

# Register your models here.


class CartListInline(admin.StackedInline):
    model = Cart
    extra = 0


class AddressInline(admin.StackedInline):
    model = AddressCustomer
    extra = 0


class UserAdmin(admin.ModelAdmin):
    inlines = [
        CartListInline,
        AddressInline,
    ]


admin.site.register(User, UserAdmin)
admin.site.register(Cart)
admin.site.register(AddressCustomer)
