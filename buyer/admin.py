# admin.py
from django.contrib import admin
from .models import Order, OrderItem, Cart

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)