# Generated by Django 4.2.3 on 2023-07-13 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0008_remove_issuebook_is_borrowed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 21, 14, 34, 24, 420863)),
        ),
    ]
