# Generated by Django 4.1.4 on 2022-12-20 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('data_carga', models.DateField()),
                ('qt_planejada', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Atividade',
        ),
        migrations.DeleteModel(
            name='Campo',
        ),
    ]
