# Generated by Django 2.2.6 on 2019-11-18 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_auto_20191118_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_categories',
            name='Cat_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='category.Main_Categories'),
        ),
    ]
