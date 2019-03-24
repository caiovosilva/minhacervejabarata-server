from django.db import models

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    descricao = models.CharField(max_length=50)
    ml = models.FloatField(null=False)

    def __str__(self):
        return self.descricao

class Produto(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    valor = models.FloatField(null=False)

    def __str__(self):
        return self.valor

class Cesta(models.Model):
    nome = models.CharField(max_length=50)
    data = models.DateField()

    def __str__(self):
        return self.nome

class ItemCesta(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cesta = models.ForeignKey(Cesta, on_delete=models.CASCADE)

    def __str__(self):
        return self.produto + self.cesta
