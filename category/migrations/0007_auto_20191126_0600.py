# Generated by Django 2.2.6 on 2019-11-26 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_auto_20191122_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_categories',
            name='Feature',
        ),
        migrations.DeleteModel(
            name='Feature_Value',
        ),
        migrations.DeleteModel(
            name='Features',
        ),
    ]
