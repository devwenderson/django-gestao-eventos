from rest_framework import serializers
from apps.eventos.models import Evento

class EventoReadSerializer(serializers.ModelSerializer):
    cliente = serializers.CharField(source="cliente.nome")
    class Meta:
        model = Evento
        fields = ["id","nome", "cliente", "data_inicio", "hora_inicio", "data_fim", "hora_fim", "status", "local"]

class EventoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = "__all__"

