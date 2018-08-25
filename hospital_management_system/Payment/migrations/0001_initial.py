# Generated by Django 2.1 on 2018-08-24 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pres_name', models.CharField(max_length=200)),
                ('pres_description', models.TextField()),
                ('pres_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('prescription_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Payment.Prescription')),
                ('total', models.IntegerField()),
            ],
            bases=('Payment.prescription',),
        ),
    ]
