# Generated by Django 5.0.6 on 2024-06-07 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Inventario', '0036_alter_acsses_point_sitecontroller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acsses_point',
            name='sitecontroller',
        ),
    ]
