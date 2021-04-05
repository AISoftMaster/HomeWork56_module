from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=2000, blank=True)
    CHOISES = (('US', 'UnitedStates'), ('FR', 'France'), ('KR', 'Kyrgyzstan'),)
    category = models.CharField(max_length=35, choices=CHOISES)
    surplus = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=1)

    def __str__(self):
        return self.name


class Basket(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='products_in_basket')
    amount = models.PositiveIntegerField()

    def __str__(self):
        return '{}:{}'.format(self.product, self.amount)


class OrderProduct(models.Model):
    product = models.ForeignKey('webapp.Product', verbose_name='продукт', on_delete=models.CASCADE)
    surplus = models.PositiveIntegerField()
    order = models.ForeignKey('webapp.Order', verbose_name='продукт', on_delete=models.CASCADE)


class Order(models.Model):
    product = models.ManyToManyField('webapp.Product', related_name='product_order', verbose_name='продукт',
                                     through='webapp.OrderProduct', through_fields=('order', 'product'))
    username = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=25, blank=False)
    address = models.CharField(max_length=100, blank=False)
    date = models.DateField(auto_now_add=True)
