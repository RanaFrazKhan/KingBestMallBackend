# Generated by Django 2.2.6 on 2019-11-01 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storebankinformation',
            name='StoreID',
            field=models.ForeignKey(db_column='StoreName', on_delete=django.db.models.deletion.CASCADE, related_name='StoreID', to='vendor.VendorStoreInformation', to_field='StoreName'),
        ),
    ]