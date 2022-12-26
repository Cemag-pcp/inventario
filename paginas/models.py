from django.db import models

# Create your models here.

class tb_balanco(models.Model):
    codigo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    familia = models.CharField(max_length=50, verbose_name='Familia')
    qt = models.IntegerField()

    class Meta:
        db_table = 'paginas_tb_balanco'
    