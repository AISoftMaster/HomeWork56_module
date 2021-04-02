# Generated by Django 3.1.7 on 2021-04-02 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('US', 'UnitedStates'), ('FR', 'France'), ('KR', 'Kyrgyzstan')], max_length=35),
        ),
    ]
