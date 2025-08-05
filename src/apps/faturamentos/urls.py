from django.urls import path
from apps.faturamentos.views import faturamentos_list

urlpatterns = [
    path("faturamentos/", faturamentos_list)
]