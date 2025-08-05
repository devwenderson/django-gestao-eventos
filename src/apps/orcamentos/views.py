from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.orcamentos.models import Orcamento
from apps.orcamentos.serializers import OrcamentoReadSerializer, OrcamentoWriteSerializer

@api_view(["GET", "POST"])
def orcamentos_list(request):
    if request.method == "GET":
        orcamentos = Orcamento.objects.all()
        serializer = OrcamentoReadSerializer(orcamentos, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = OrcamentoWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "DELETE", "PUT"])
def orcamentos_detail(request, pk):
    try:
        orcamento = Orcamento.objects.get(pk=pk)
    except Orcamento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = OrcamentoReadSerializer(orcamento)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        orcamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        serializer = OrcamentoWriteSerializer(orcamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

