# Generated by Django 2.2.6 on 2019-11-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productsreviews_recently_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count_no',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
