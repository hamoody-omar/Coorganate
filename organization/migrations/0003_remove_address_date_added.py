# Generated by Django 2.2.3 on 2019-07-11 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_organaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='date_added',
        ),
    ]
