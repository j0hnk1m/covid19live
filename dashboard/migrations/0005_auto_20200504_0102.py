# Generated by Django 3.0.3 on 2020-05-04 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200503_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='slug',
            field=models.CharField(max_length=50),
        ),
    ]