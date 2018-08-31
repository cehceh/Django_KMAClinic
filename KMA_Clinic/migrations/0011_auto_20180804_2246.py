# Generated by Django 2.0.5 on 2018-08-04 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KMA_Clinic', '0010_auto_20180804_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kma',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='kma',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='visits',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KMA_Clinic.KMA'),
        ),
    ]