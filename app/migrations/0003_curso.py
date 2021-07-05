# Generated by Django 3.2.5 on 2021-07-05 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alumno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del curso')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.docente')),
            ],
            options={
                'verbose_name': 'curso',
                'verbose_name_plural': 'cursos',
                'db_table': 'cursos',
                'ordering': ['id'],
            },
        ),
    ]
