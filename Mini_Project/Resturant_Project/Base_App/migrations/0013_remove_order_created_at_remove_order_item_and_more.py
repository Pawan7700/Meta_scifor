# Generated by Django 5.1 on 2024-10-01 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0012_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
    ]
