from datetime import date 
from django.db import models
from apps.eventos.models import Evento


class Orcamento(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("concluido", "Concluído"),
        ("cancelado", "Cancelado"),
    ]

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="orcamento")
    valor = models.DecimalField(verbose_name="Valor", max_digits=10, decimal_places=2, null=True, blank=True)
    data_criacao = models.DateField(verbose_name="Data de criação", auto_now_add=True)
    status = models.CharField(verbose_name="Status", max_length=20)
    numero_faturamentos = models.PositiveIntegerField(verbose_name="Número de faturamentos")

    class Meta:
        verbose_name = "Orcamento"
        verbose_name_plural = "Orcamentos"
        ordering = ["-data_criacao"]
        db_table = "tb_orcamentos"

    def save(self, *args, **kwargs):
        if self.numero_faturamentos:
            valor = self.valor / self.numero_faturamentos
            data = date.today() 
            for i in range(1, self.numero_faturamentos+1):
                faturamento = self.faturamentos.create(
                    orcamento=self.id,
                    data_vencimento=f"{data.year}-{data.month+i}-{data.day}",
                    valor=valor
                )
                faturamento.save()     
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Orçamento {self.id}: {self.evento.nome}"
    
