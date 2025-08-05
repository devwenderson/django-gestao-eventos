from rest_framework import serializers
from apps.orcamentos.models import Orcamento
from apps.eventos.models import Evento

class OrcamentoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orcamento
        fields = "__all__" #("evento", "valor", "data_criacao", "status")
    
class OrcamentoReadSerializer(serializers.ModelSerializer):

    class EventoOrcamentoList(serializers.ModelSerializer):
        cliente = serializers.CharField(source="cliente.nome", read_only=True)
        class Meta:
            model = Evento
            fields = ["nome", "cliente", "data_inicio", "data_fim"]

    evento = EventoOrcamentoList(read_only=True)

    class Meta:
        model = Orcamento
        fields = "__all__"