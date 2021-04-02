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
        return '{}:{}'.format(self.name, self.surplus)
