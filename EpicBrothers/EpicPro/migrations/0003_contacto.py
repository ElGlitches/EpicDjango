# Generated by Django 3.1.2 on 2020-11-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EpicPro', '0002_juegos_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'consulta'], [1, 'reclamo'], [2, 'sugerencia'], [3, 'felicitaciones']])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
    ]
