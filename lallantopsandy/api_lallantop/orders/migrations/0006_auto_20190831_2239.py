# Generated by Django 2.2.4 on 2019-08-31 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190831_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.EmailField(blank=True, default='ff@gmail.com', max_length=254),
        ),
    ]
