# Generated by Django 2.0.1 on 2018-02-02 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0009_merge_20180202_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoreo',
            name='titulo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='monitoreo',
            name='url',
            field=models.URLField(),
        ),
    ]
