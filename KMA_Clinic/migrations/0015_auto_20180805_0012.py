# Generated by Django 2.0.5 on 2018-08-04 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KMA_Clinic', '0014_auto_20180805_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visits',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KMA_Clinic.KMA'),
        ),
    ]
