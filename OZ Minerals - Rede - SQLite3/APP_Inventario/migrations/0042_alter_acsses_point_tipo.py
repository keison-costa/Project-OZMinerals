# Generated by Django 5.0.6 on 2024-06-08 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Inventario', '0041_alter_acsses_point_sitecontroller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acsses_point',
            name='tipo',
            field=models.CharField(choices=[('ACSSES POINT', 'ACSSES POINT'), ('PTP', 'PTP')], max_length=50, verbose_name='Tipo'),
        ),
    ]
