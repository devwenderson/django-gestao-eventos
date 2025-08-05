from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.faturamentos.models import Faturamento
from apps.faturamentos.serializers import FaturamentoReadSerializer, FaturamentoWriteSerializer

@api_view(["GET", "POST"])
def faturamentos_list(request):
    if request.method == "GET":
        faturamentos = Faturamento.objects.all()
        serializer = FaturamentoReadSerializer(faturamentos, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = FaturamentoWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)