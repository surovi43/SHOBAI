# Generated by Django 5.1.1 on 2024-11-21 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='SKU',
            new_name='sku',
        ),
    ]
