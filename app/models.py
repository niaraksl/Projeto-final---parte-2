from django.db import models


class Produto(models.Model):
    nome_produto = models.CharField('Nome do produto', max_length=100)

    def __str__(self):
        return self.nome_produto