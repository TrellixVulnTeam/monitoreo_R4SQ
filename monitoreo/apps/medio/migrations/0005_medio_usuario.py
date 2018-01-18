# Generated by Django 2.0.1 on 2018-01-05 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('medio', '0004_remove_medio_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='medio',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario'),
        ),
    ]
