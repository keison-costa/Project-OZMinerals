# Generated by Django 5.0.6 on 2024-06-17 15:22

import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aparelhos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IMEI_APARELHO', models.CharField(max_length=15, unique=True, verbose_name='IMEI do Telefone')),
                ('MODELO', models.CharField(max_length=20, verbose_name='Modelo')),
                ('FABRICANTE', models.CharField(max_length=20, verbose_name='Fabricante')),
                ('UTILIZADOR', models.CharField(max_length=50, verbose_name='Nome Completo do Utilizador')),
                ('EMAIL', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('LOGIN_ADMANAGER', models.CharField(max_length=50, unique=True, verbose_name='Login ADManager')),
            ],
            options={
                'verbose_name': 'Aparelho',
                'verbose_name_plural': 'Aparelhos',
            },
        ),
        migrations.CreateModel(
            name='LinhaTelefonica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Número de Telefone')),
                ('imei_number', models.CharField(max_length=15, unique=True, verbose_name='IMEI do CHIP')),
                ('registration_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data/Hora de Registro')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP_TeleLinhas.aparelhos', verbose_name='Selecione o Aparelho')),
            ],
            options={
                'verbose_name': 'Linha Telefônica',
                'verbose_name_plural': 'Linhas Telefônicas',
            },
        ),
    ]
