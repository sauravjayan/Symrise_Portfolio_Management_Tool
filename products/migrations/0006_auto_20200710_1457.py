# Generated by Django 3.0.3 on 2020-07-10 14:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200705_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='additonal_info',
        ),
        migrations.RemoveField(
            model_name='product',
            name='regulatory_info',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='technical_info',
        ),
        migrations.AddField(
            model_name='product',
            name='alcohol_content',
            field=models.FloatField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='product',
            name='arrival_date',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='expiry_date',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='halal_status',
            field=models.CharField(choices=[('Contains alcohol', 'Contains alcohol'), ('Inconsistent data', 'Inconsistent data'), ('Halal suitable', 'Halal suitable'), ('Not Halal', 'Not Halal')], default='Halal Suitable', max_length=256),
        ),
        migrations.AddField(
            model_name='product',
            name='lab_location',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='legal_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='order_date',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='physical_form',
            field=models.CharField(choices=[('Liquid', 'Liquid'), ('Spray Dried', 'Spray Dried'), ('Viscous/Paste', 'Viscous/Paste'), ('Wash', 'Wash')], max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='portfolio_manager',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='production_site',
            field=models.CharField(choices=[('Holzminden', 'Holzminden'), ('Noerdlingen', 'Noerdlingen'), ('Braunschweig', 'Braunschweig'), ('Egypt', 'Egypt')], max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sales_status',
            field=models.CharField(choices=[('FS', 'FS'), ('CR', 'CR'), ('CC', 'CC'), ('CE', 'CE'), ('CD', 'CD'), ('CT', 'CT')], max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='shelf_life',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='solubility',
            field=models.CharField(choices=[('Oil soluble', 'Oil soluble'), ('Water soluble', 'Water soluble'), ('Water dispersible', 'Water dispersable')], max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='storage_condition',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
