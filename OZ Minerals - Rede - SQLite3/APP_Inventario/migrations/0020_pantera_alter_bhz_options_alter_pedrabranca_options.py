# Generated by Django 5.0.6 on 2024-06-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Inventario', '0019_alter_can_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='PANTERA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VLAN', models.CharField(blank=True, max_length=50, null=True, verbose_name='VLAN')),
                ('SERIAL', models.CharField(blank=True, max_length=50, null=True, verbose_name='SERIAL')),
                ('SERVICE_TAG', models.CharField(blank=True, max_length=50, null=True, verbose_name='SERVICE TAG')),
                ('MODEL_HOST', models.CharField(blank=True, max_length=50, null=True, verbose_name='MODEL / HOST')),
                ('TYPE', models.CharField(blank=True, max_length=50, null=True, verbose_name='TYPE')),
                ('NAME', models.CharField(blank=True, max_length=50, null=True, verbose_name='NAME')),
                ('IP', models.CharField(blank=True, max_length=50, null=True, verbose_name='IP ADDRESS')),
                ('HOSTNAME', models.CharField(blank=True, max_length=50, null=True, verbose_name='HOSTNAME')),
                ('MAC', models.CharField(blank=True, max_length=50, null=True, verbose_name='M.A.C')),
                ('LOCAL_COMMENT', models.CharField(blank=True, max_length=50, null=True, verbose_name='LOCAL (COMMENT)')),
                ('SWITCH_PORT', models.CharField(blank=True, max_length=50, null=True, verbose_name='SWITCH PORT')),
                ('DHCP_OPTION', models.CharField(blank=True, max_length=50, null=True, verbose_name='DHCP OPTION')),
            ],
            options={
                'verbose_name': 'PANTERA',
                'verbose_name_plural': 'PANTERA',
            },
        ),
        migrations.AlterModelOptions(
            name='bhz',
            options={'verbose_name': 'BELORIZONTE', 'verbose_name_plural': 'BELORIZONTE'},
        ),
        migrations.AlterModelOptions(
            name='pedrabranca',
            options={'verbose_name': 'PEDRA BRANCA', 'verbose_name_plural': 'PEDRA BRANCA'},
        ),
    ]