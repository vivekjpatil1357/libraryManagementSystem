# Generated by Django 4.2.3 on 2023-07-13 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0006_remove_bookinstance_is_borrowed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 21, 13, 59, 35, 798084)),
        ),
    ]
