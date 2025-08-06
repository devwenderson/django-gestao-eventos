from django.db import models
from apps.orcamentos.models import Orcamento

class Faturamento(models.Model):
    STATUS_CHOICES = [
        ("em andamento", "Em andamento"),
        ("pago", "Pago"),
        ("atrasado", "Atrasado")
    ]
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE, related_name="faturamentos")
    data_vencimento = models.DateField(verbose_name="Data de vencimento")
    data_pagamento = models.DateField(verbose_name="Data de pagamento", null=True, blank=True)
    status = models.CharField(verbose_name="Status", max_length=15, choices=STATUS_CHOICES)
    valor = models.DecimalField(verbose_name="Valor", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id} - {self.orcamento.id}"
    

