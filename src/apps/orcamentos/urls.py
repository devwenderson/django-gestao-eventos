from django.urls import path
from apps.orcamentos.views import orcamentos_list, orcamentos_detail

urlpatterns = [
    path("orcamentos/", orcamentos_list),
    path("orcamentos/<int:pk>/", orcamentos_detail),
]