from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.clientes.models import Cliente
from apps.clientes.serializers import ClienteSerializer

@api_view(["GET", "POST"])
def clientes_list(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def clientes_detail(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        cliente.delete()
        return Response(status=status.HTTP_204_NOT_CONTENT)