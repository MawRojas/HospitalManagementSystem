# Generated by Django 2.1 on 2018-08-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0003_doctors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='shift',
            field=models.BigIntegerField(blank=True, default='', max_length=100000),
        ),
    ]
