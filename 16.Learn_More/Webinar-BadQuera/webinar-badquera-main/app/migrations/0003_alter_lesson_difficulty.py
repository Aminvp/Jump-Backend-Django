# Generated by Django 3.2.5 on 2021-07-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210708_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='difficulty',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
