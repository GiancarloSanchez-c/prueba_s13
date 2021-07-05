# Generated by Django 3.2.5 on 2021-07-05 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firts_name', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido Materno')),
                ('name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('date_birth', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
            ],
            options={
                'verbose_name': 'alumno',
                'verbose_name_plural': 'alumnos',
                'db_table': 'alumno',
                'ordering': ['id'],
            },
        ),
    ]
