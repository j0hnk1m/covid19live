# Generated by Django 3.0.4 on 2020-04-25 22:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20200425_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='latitude',
            field=models.DecimalField(decimal_places=18, max_digits=20, unique=True, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)]),
        ),
        migrations.AlterField(
            model_name='province',
            name='longitude',
            field=models.DecimalField(decimal_places=19, max_digits=21, unique=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)]),
        ),
        migrations.AlterField(
            model_name='province',
            name='name',
            field=models.CharField(default='nan', max_length=50, unique=True),
        ),
    ]
