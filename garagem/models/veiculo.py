from django.db import models

from garagem.models import Cor, Modelo

class Veiculo(models.Model):
    modelo = models.ForeignKey(
        Modelo, on_delete=models.PROTECT, related_name="veiculo"
    )
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="veiculo"
    )
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    descricao = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.modelo} {self.ano} {self.cor}'
