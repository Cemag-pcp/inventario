# Generated by Django 4.1.4 on 2022-12-21 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0002_base_delete_atividade_delete_campo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Base',
            new_name='Employee',
        ),
    ]
