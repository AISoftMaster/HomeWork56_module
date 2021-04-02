from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, CreateView
from .models import Product
from .forms import ProductForm

# Create your views here.


class ProductListView(ListView):
    template_name = "product_list.html"
    context_object_name = "products"
    model = Product
    paginate_by = 10


class ProductDetailView(DeleteView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    form_class = ProductForm

    def form_valid(self, form):
        print(form)
        product = form.save(commit=False)
        product.save()
        return redirect('product_list')
