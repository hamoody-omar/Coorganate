# Generated by Django 2.2.3 on 2019-07-11 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organ', '0005_auto_20190711_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organ',
            name='date_extracted',
        ),
    ]
