# Generated by Django 3.0.3 on 2020-04-28 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0027_auto_20200427_1721'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='date',
            index=models.Index(fields=['date', 'country'], name='dashboard_d_date_21fb65_idx'),
        ),
    ]
