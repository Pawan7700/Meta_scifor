# Generated by Django 5.1 on 2024-09-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_table',
            name='Number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book_table',
            name='Person',
            field=models.IntegerField(),
        ),
    ]