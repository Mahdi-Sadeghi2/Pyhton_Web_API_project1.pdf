# Generated by Django 5.0.2 on 2024-02-19 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ('id',), 'verbose_name': 'Payment', 'verbose_name_plural': 'Payments'},
        ),
    ]
