# Generated by Django 2.2.3 on 2019-07-11 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organ', '0007_auto_20190711_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organ',
            name='date_added',
        ),
    ]
