# Generated by Django 4.0.6 on 2022-08-03 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_customer_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customer_id',
        ),
    ]