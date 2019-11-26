# Generated by Django 2.2.6 on 2019-11-06 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0003_vendorstoreinformation_isdeleted'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0004_remove_product_count_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreatedDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('inwatchlist', models.BooleanField(default=True)),
                ('ProductID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiscountCoupons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Discount', models.IntegerField()),
                ('Day', models.IntegerField()),
                ('Qty', models.IntegerField()),
                ('CouponsCode', models.CharField(max_length=255)),
                ('ProductID', models.CharField(blank=True, max_length=255)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('StoreName', models.ForeignKey(db_column='StoreName', default='Brainplow', on_delete=django.db.models.deletion.CASCADE, to='vendor.VendorStoreInformation', to_field='StoreName')),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(default=0)),
                ('incheckout', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('promocode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='watchlistAndCart.DiscountCoupons')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]