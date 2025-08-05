from django.urls import path
from apps.eventos.views import eventos_list, eventos_detail

urlpatterns = [
    path("eventos/", eventos_list),
    path("eventos/<int:pk>/", eventos_detail),
]