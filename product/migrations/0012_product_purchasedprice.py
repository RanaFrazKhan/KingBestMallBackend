# Generated by Django 2.2.6 on 2019-11-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20191114_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PurchasedPrice',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
