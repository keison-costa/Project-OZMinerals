# Generated by Django 5.0.6 on 2024-06-07 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Inventario', '0033_acsses_point_sitecontroller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acsses_point',
            name='sitecontroller',
            field=models.CharField(max_length=20, verbose_name='Site Controller'),
        ),
    ]