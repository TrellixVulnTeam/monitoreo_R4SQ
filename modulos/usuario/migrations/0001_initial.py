# Generated by Django 2.0.1 on 2018-01-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_parterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMENINO')], max_length=1)),
                ('telefono', models.IntegerField(max_length=12)),
            ],
        ),
    ]
