from django.db import models
from clientes.models import Clientes
from .choices import ChoicesCategoriaManutencao
from datetime import datetime
from secrets import token_hex

# Create your models here.

class CategoriaManutencao(models.Model):
    #É um choice onde vc faz no arquivo py
    titulo = models.CharField(max_length=3, choices=ChoicesCategoriaManutencao.choices)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.titulo


class Servico(models.Model):
    titulo = models.CharField(max_length=30)
    clientes = models.ForeignKey(Clientes, on_delete=models.SET_NULL, null=True)
    categoria_manutencao = models.ManyToManyField(CategoriaManutencao)
    data_inicio = models.DateField(null=True)
    data_fim = models.DateField(null=True)
    finalizado = models.BooleanField(default=False)
    protocolo = models.CharField(max_length=52, null=True,blank=True)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        #para quando atualizar nao muda o token
        if not self.protocolo:
            self.protocolo = datetime.now().strftime('%d/%m/%Y-%H:%M:%S-') + token_hex(16)

        super(Servico, self).save(*args, **kwargs)

    def preco_total(self):
        preco_total = float(0)
        for categoria in self.categoria_manutencao.all():
            preco_total += float(categoria.preco)

        return preco_total

