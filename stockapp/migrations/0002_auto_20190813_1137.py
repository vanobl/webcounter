# Generated by Django 2.1.6 on 2019-08-13 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comminginvoice',
            name='number',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='номер'),
        ),
    ]
