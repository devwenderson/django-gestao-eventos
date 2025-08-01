from django.urls import path
from apps.clientes.views import clientes_list, clientes_detail

urlpatterns = [
    path("clientes/", clientes_list),
    path("clientes/<int:pk>/", clientes_detail)
]