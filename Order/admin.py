from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['ItemProductName', 'ItemPrice', 'ItemQuantity', 'ItemTotalPrice']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['OrderNo', 'OrderUser', 'OrderTotalPrice', 'OrderStatus', 'OrderPayMethod', 'CreateTime']
    list_editable = ['OrderStatus']
    list_filter = ['OrderStatus', 'OrderPayMethod']
    search_fields = ['OrderNo', 'OrderUser__username', 'OrderReceiver']
    readonly_fields = ['OrderNo', 'OrderTotalPrice']
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['ItemOrder', 'ItemProductName', 'ItemPrice', 'ItemQuantity', 'ItemTotalPrice']
    search_fields = ['ItemProductName']
