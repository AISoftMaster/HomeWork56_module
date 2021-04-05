from django import forms
from webapp.models import Product, Basket, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'surplus', 'price',)


class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ('amount',)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('username', 'phone_number', 'address',)
