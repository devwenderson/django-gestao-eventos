from django.db import models

class Cliente(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=65, null=True, blank=True)
    telefone = models.CharField(verbose_name="Telefone", max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.nome}"
