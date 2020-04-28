# Generated by Django 3.0.3 on 2020-04-28 02:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0028_auto_20200427_1745'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='date',
            name='dashboard_d_date_21fb65_idx',
        ),
        migrations.RemoveField(
            model_name='date',
            name='date',
        ),
        migrations.AddField(
            model_name='date',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 28, 2, 43, 55, 403662, tzinfo=utc), verbose_name='datetime'),
            preserve_default=False,
        ),
        migrations.AddIndex(
            model_name='date',
            index=models.Index(fields=['datetime', 'country'], name='dashboard_d_datetim_56cdc0_idx'),
        ),
    ]
