# Generated by Django 5.0.6 on 2024-06-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Inventario', '0039_alter_acsses_point_sitecontroller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acsses_point',
            name='sitecontroller',
            field=models.CharField(choices=[('Oz-Homolog', 'Oz-Homolog'), ('PBA-MINA', 'PBA-MINA'), ('PBA-PRONTOS', 'PBA-PRONTOS'), ('Pedra Branca', 'Pedra Branca')], max_length=30, verbose_name='Site na Controller'),
        ),
    ]
