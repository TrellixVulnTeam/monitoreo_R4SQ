# Generated by Django 2.0.1 on 2018-01-05 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=12),
        ),
    ]
