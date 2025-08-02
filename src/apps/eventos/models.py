from django.db import models
from apps.clientes.models import Cliente

class Evento(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("concluido", "Concluído"),
        ("cancelado", "Cancelado"),
    ]

    nome = models.CharField(verbose_name="Nome do evento", max_length=100, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="eventos")
    data_inicio = models.DateField(verbose_name="Data de início", null=True, blank=True)
    hora_inicio = models.TimeField(verbose_name="Hora de início", null=True, blank=True)
    data_fim = models.DateField(verbose_name="Data de fim", null=True, blank=True)
    hora_fim = models.TimeField(verbose_name="Hora de fim", null=True, blank=True)
    status = models.CharField(verbose_name="Status do evento", max_length=20, choices=STATUS_CHOICES, default="pendente")
    local = models.CharField(verbose_name="Local", max_length=65, null=True, blank=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ["data_inicio"]

    def __str__(self):
        return f"{self.nome} - {self.data_inicio} - {self.hora_inicio}"
    
    def save(self, *args, **kwargs):
        if not(self.nome) and self.cliente:
            self.nome = f"Evento de {self.cliente.nome}"
        super().save(*args, **kwargs)


