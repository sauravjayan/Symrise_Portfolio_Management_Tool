# Generated by Django 3.0.3 on 2020-07-05 14:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('regulatory_info', '0001_initial'),
        ('additional_info', '0001_initial'),
        ('technical_info', '0001_initial'),
        ('stock', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='additonal_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='additional_info.AdditionalInfo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='regulatory_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='regulatory_info.RegulatoryInfo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, related_name='product', to='stock.Stock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='technical_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='technical_info.TechnicalInfo'),
            preserve_default=False,
        ),
    ]
