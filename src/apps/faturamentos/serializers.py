from rest_framework import serializers
from apps.faturamentos.models import Faturamento

class FaturamentoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faturamento
        fields = "__all__"

class FaturamentoReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faturamento
        fields = ["id", "orcamento", "data_vencimento", "data_pagamento"]