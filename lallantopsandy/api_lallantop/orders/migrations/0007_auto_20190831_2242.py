# Generated by Django 2.2.4 on 2019-08-31 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20190831_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='phone_number',
            new_name='contact',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='email',
        ),
    ]