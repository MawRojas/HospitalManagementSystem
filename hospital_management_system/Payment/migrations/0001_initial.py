# Generated by Django 2.1 on 2018-08-29 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
        ('Surgery_Details', '0001_initial'),
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_status', models.CharField(max_length=50)),
                ('total', models.IntegerField()),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bill', to='Person.Patient')),
                ('patient_room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bill', to='hospital.PatientRoom')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pres_name', models.CharField(max_length=200)),
                ('pres_description', models.TextField()),
                ('pres_price', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='prescription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bill', to='Payment.Prescription'),
        ),
        migrations.AddField(
            model_name='bill',
            name='surgery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bill', to='Surgery_Details.Surgery'),
        ),
    ]