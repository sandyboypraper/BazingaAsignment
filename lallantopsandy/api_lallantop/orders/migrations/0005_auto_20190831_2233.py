# Generated by Django 2.2.4 on 2019-08-31 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_orders_goto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='price',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
