# Generated by Django 5.0.6 on 2024-06-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Inventario', '0016_pedrabranca_model_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='VLANs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VLAN', models.CharField(blank=True, max_length=50, null=True, verbose_name='VLAN')),
                ('NAME', models.CharField(blank=True, max_length=50, null=True, verbose_name='NAME')),
                ('NAME_OBS', models.CharField(blank=True, max_length=50, null=True, verbose_name='NAME-OBS')),
                ('OUTROS', models.CharField(blank=True, max_length=50, null=True, verbose_name='OUTROS')),
                ('OUTROS_OBS', models.CharField(blank=True, max_length=50, null=True, verbose_name='OUTROS-OBS')),
            ],
            options={
                'verbose_name': 'VLANs',
                'verbose_name_plural': 'VLANs',
            },
        ),
    ]