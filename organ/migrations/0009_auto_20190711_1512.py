# Generated by Django 2.2.3 on 2019-07-11 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organ', '0008_remove_organ_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
