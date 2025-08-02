from django.urls import path
from apps.eventos.views import eventos_list

urlpatterns = [
    path("eventos/", eventos_list),
]