# Generated by Django 2.1 on 2018-08-27 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20180824_1451'),
        ('Person', '0002_remove_nurses_patientrooms'),
        ('Surgery_Details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='surgery',
            name='doctor_incharge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='surgery', to='Person.Doctors'),
        ),
        migrations.AddField(
            model_name='surgery',
            name='nurse_incharge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='surgery', to='Person.Nurses'),
        ),
        migrations.AddField(
            model_name='surgery',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='surgery', to='Person.Patient'),
        ),
        migrations.AddField(
            model_name='surgery',
            name='surgery_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='surgery', to='hospital.SurgeryRoom'),
        ),
    ]
