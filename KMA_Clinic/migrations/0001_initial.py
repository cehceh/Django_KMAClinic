# Generated by Django 2.0.5 on 2018-07-14 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('birthdate', models.DateTimeField(verbose_name='Birth Date')),
                ('age', models.CharField(max_length=100)),
                ('phone', models.IntegerField(default=0)),
                ('husband', models.CharField(max_length=100)),
            ],
        ),
    ]
