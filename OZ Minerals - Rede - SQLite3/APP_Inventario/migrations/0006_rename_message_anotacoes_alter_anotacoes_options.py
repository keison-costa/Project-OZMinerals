# Generated by Django 5.0.6 on 2024-06-02 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Inventario', '0005_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='anotacoes',
        ),
        migrations.AlterModelOptions(
            name='anotacoes',
            options={'verbose_name': 'Anotações', 'verbose_name_plural': 'Anotações'},
        ),
    ]
