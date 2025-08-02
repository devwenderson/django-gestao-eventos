from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.eventos.models import Evento
from apps.eventos.serializers import EventoReadSerializer, EventoWriteSerializer

@api_view(["GET", "POST"])
def eventos_list(request):
    if request.method == "GET":
        eventos = Evento.objects.all()
        serializer = EventoReadSerializer(eventos, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = EventoWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)