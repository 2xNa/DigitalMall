from django.contrib import admin
from .models import CartItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['CartUser', 'CartProduct', 'CartQuantity', 'CartIsSelected', 'CreateTime']
    list_filter = ['CartIsSelected']
    search_fields = ['CartUser__username', 'CartProduct__ProductName']
