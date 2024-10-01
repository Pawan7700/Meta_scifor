# Generated by Django 5.1 on 2024-10-01 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0013_remove_order_created_at_remove_order_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default='Not provided'),
        ),
        migrations.AddField(
            model_name='order',
            name='contact_number',
            field=models.CharField(default='0000000000', max_length=15),
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default='2024-01-01 00:00:00'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Base_App.items'),
        ),
        migrations.AddField(
            model_name='order',
            name='pincode',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
