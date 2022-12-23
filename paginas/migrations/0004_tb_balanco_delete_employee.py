# Generated by Django 4.1.4 on 2022-12-22 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0003_rename_base_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_balanco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('familia', models.CharField(max_length=50, verbose_name='Descrição')),
                ('qt', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]