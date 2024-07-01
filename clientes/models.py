from django.db import models

# Create your models here.


class Clientes(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    cpf = models.CharField(max_length=12)

    def __str__(self):
        return self.nome


class Carros(models.Model):
    carro = models.CharField(max_length=50)
    placa = models.CharField(max_length=10)
    ano = models.IntegerField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    lavagen = models.IntegerField(default=0)
    conserto = models.IntegerField(default=0)

    def __str__(self):
        return self.carro

#makemigration faz um arquivo para dizer oque tem que ter no meu banco de dados
