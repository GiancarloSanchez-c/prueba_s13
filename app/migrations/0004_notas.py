# Generated by Django 3.2.5 on 2021-07-05 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nota_1', models.IntegerField(verbose_name='Nota 1')),
                ('nota_2', models.IntegerField(verbose_name='Nota 2')),
                ('nota_3', models.IntegerField(verbose_name='Nota 3')),
                ('nota_4', models.IntegerField(verbose_name='Nota 4')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
            ],
            options={
                'verbose_name': 'nota',
                'verbose_name_plural': 'notas',
                'db_table': 'notas',
                'ordering': ['id'],
            },
        ),
    ]