from datetime import date
from dateutil.relativedelta import relativedelta
from django.db import models
from apps.eventos.models import Evento

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Orcamento(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("concluido", "Concluído"),
        ("cancelado", "Cancelado"),
    ]

    evento = models.OneToOneField(Evento, on_delete=models.CASCADE, related_name="orcamento")
    valor = models.DecimalField(verbose_name="Valor", max_digits=10, decimal_places=2, null=True, blank=True)
    data_criacao = models.DateField(verbose_name="Data de criação", auto_now_add=True)
    status = models.CharField(verbose_name="Status", max_length=20)
    numero_faturamentos = models.PositiveIntegerField(verbose_name="Número de faturamentos")

    class Meta:
        verbose_name = "Orcamento"
        verbose_name_plural = "Orcamentos"
        db_table = "tb_orcamentos"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # Tem que vir no início nesse casoS
        if self.numero_faturamentos:
            valor = self.valor / self.numero_faturamentos
            data = date.today() 
            for i in range(1, self.numero_faturamentos+1):
                data_vencimento = data + relativedelta(months=i)
                faturamento = self.faturamentos.create(
                    data_vencimento=f"{data_vencimento}",
                    valor=valor,
                    status="em andamento"
                )


    def __str__(self):
        return f"Orçamento {self.id}: {self.evento.nome}"
    
