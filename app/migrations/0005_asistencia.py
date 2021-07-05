# Generated by Django 3.2.5 on 2021-07-05 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_notas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('A', 'Asistió'), ('F', 'Faltó'), ('T', 'Tardanza')], default='Asistió', max_length=10)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
            ],
            options={
                'verbose_name': 'asistencia',
                'verbose_name_plural': 'asistencias',
                'db_table': 'asistencia',
                'ordering': ['id'],
            },
        ),
    ]
