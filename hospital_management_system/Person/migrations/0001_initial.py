# Generated by Django 2.1 on 2018-08-29 12:10

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=200)),
                ('social', models.CharField(max_length=200)),
                ('shift', models.CharField(blank=True, default='', max_length=200)),
                ('jobDesc', models.CharField(blank=True, default='', max_length=200)),
                ('salary', models.DecimalField(decimal_places=0, default=Decimal('0.00'), max_digits=7)),
                ('specialty', models.CharField(blank=True, default='', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nurses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=200)),
                ('social', models.CharField(max_length=200)),
                ('shift', models.CharField(blank=True, default='', max_length=200)),
                ('jobDesc', models.CharField(blank=True, default='', max_length=200)),
                ('salary', models.DecimalField(decimal_places=0, default=Decimal('0.00'), max_digits=7)),
                ('specialty', models.CharField(blank=True, default='', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=200)),
                ('social', models.CharField(max_length=200)),
                ('symptoms', models.CharField(blank=True, default='', max_length=200)),
                ('allergies', models.CharField(blank=True, default='', max_length=200)),
                ('currentMeds', models.CharField(blank=True, default='', max_length=200)),
                ('docName', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Person.Doctors')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
