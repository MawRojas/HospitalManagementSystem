# Generated by Django 2.1 on 2018-08-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20180827_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surgeryroom',
            name='equipment',
            field=models.ManyToManyField(blank=True, null=True, to='Surgery_Details.Equipment'),
        ),
    ]