# Generated by Django 5.0.2 on 2024-02-19 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitem',
            options={'ordering': ('id',), 'verbose_name': 'Cart Item', 'verbose_name_plural': 'Cart Items'},
        ),
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'ordering': ('id',), 'verbose_name': 'shopping Cart', 'verbose_name_plural': 'shopping Carts'},
        ),
    ]
