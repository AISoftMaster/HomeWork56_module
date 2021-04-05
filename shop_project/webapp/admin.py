from django.contrib import admin
from .models import Product, Basket, Order, OrderProduct

# Register your models here.
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(Order)
admin.site.register(OrderProduct)
