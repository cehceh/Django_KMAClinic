# Generated by Django 2.0.5 on 2018-08-03 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KMA_Clinic', '0002_visits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visits',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KMA_Clinic.KMA'),
        ),
    ]
