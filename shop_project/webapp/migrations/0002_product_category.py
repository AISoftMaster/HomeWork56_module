# Generated by Django 3.1.7 on 2021-04-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default=12, max_length=35),
            preserve_default=False,
        ),
    ]
