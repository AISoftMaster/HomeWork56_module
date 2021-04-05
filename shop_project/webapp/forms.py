from django import forms
from webapp.models import Product, Basket


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'surplus', 'price',)


class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ('amount',)
