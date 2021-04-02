from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.


class ProductListView(ListView):
    template_name = "product_list.html"
    context_object_name = "products"
    model = Product
    paginate_by = 10
