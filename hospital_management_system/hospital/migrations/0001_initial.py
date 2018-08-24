# Generated by Django 2.1 on 2018-08-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PatientRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.BigIntegerField(default=0)),
                ('is_occupied', models.BooleanField(default='0')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SurgeryRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.BigIntegerField(default=0)),
                ('is_occupied', models.BooleanField(default='0')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='hospital',
            name='patient_rooms',
            field=models.ManyToManyField(to='hospital.PatientRoom'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='surgery_rooms',
            field=models.ManyToManyField(to='hospital.SurgeryRoom'),
        ),
    ]