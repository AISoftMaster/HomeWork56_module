from django.contrib import admin
from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView, \
    AddBasket, BasketListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/basket/', AddBasket.as_view(), name='basket_update'),
    path('basket', BasketListView.as_view(), name='basket_list'),
]
