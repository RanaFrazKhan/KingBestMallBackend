# Generated by Django 2.2.6 on 2019-11-18 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_sub_sub_categories_cat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_categories',
            name='Cat_Des',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='main_categories',
            name='Pic',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sub_categories',
            name='Pic',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sub_categories',
            name='Subcat_Des',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sub_sub_categories',
            name='Pic',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sub_sub_categories',
            name='Sub_Subcat_Des',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]