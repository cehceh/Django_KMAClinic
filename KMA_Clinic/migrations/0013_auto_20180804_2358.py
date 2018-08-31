# Generated by Django 2.0.5 on 2018-08-04 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KMA_Clinic', '0012_auto_20180804_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kma',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='visits',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KMA_Clinic.KMA'),
        ),
    ]
