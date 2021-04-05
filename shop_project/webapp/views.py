from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Product, Basket
from .forms import ProductForm, BasketForm, OrderForm

# Create your views here.


class ProductListView(ListView):
    template_name = "product_list.html"
    context_object_name = "products"
    model = Product
    paginate_by = 5


class ProductDetailView(DetailView):
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


class ProductDeleteView(DeleteView):
    template_name = 'product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    form_class = ProductForm
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class AddBasket(CreateView):
    model = Basket
    template_name = 'basket_input.html'
    context_object_name = 'basket'
    form_class = BasketForm

    def get_context_data(self, **kwargs):
        kwargs['product'] = Product.objects.get(pk=self.kwargs.get('pk'))
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        product = Product.objects.get(pk=self.kwargs.get('pk'))
        if product.surplus > form.cleaned_data.get('amount'):
            try:
                basket = Basket.objects.get(product__pk=product.pk)
                basket.amount += form.cleaned_data.get("amount")
                basket.save()
            except Basket.DoesNotExist:
                Basket.objects.create(product=product, amount=form.cleaned_data.get("amount"))
            product.surplus -= form.cleaned_data.get('amount')
            product.save()
        return redirect('product_list')


class BasketListView(ListView):
    template_name = 'basket_list.html'
    context_object_name = 'baskets'
    model = Basket
    paginate_by = 5
    # form_class = OrderForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = OrderForm()
        return context

    def post(self, request, *args, **kwargs):
        form = OrderForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('username'))
            return redirect('basket_list')



class BasketDeleteView(DeleteView):
    template_name = 'basket_delete.html'
    model = Basket
    context_object_name = 'basket'
    success_url = reverse_lazy('basket_list')

