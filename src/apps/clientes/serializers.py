from rest_framework import serializers
from apps.clientes.models import Cliente
from apps.eventos.serializers import EventoReadSerializer

from apps.eventos.models import Evento

class ClienteReadSerializer(serializers.ModelSerializer):
    # PARA LISTAR EVENTOS DOS CLIENTES
    class EventoClienteListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Evento
            fields = ["nome", "local", "status", "data_inicio", "data_fim"]

    eventos = EventoClienteListSerializer(many=True, read_only=True)
    class Meta:
        model = Cliente
        fields = ["id","nome", "telefone", "eventos"]

class ClienteWriteSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Cliente
        fields = "__all__"