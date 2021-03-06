# Generated by Django 2.2.2 on 2019-07-10 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KMA_Clinic', '0016_auto_20180805_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kma',
            name='birthdate',
            field=models.DateField(null=True, verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='visits',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KMA_Clinic.KMA'),
        ),
    ]
