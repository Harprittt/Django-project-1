# Generated by Django 4.0.6 on 2022-07-29 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_remove_customer_image_remove_customer_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
