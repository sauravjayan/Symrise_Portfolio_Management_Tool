# Generated by Django 3.0.3 on 2020-07-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200705_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='wlc',
            field=models.BooleanField(null=True, verbose_name='Winning Local Collection'),
        ),
    ]
