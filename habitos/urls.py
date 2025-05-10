from django.urls import path, include
from .views import HabitoView, HabitoDetailView

urlpatterns = [
    path('agenda/',HabitoView.as_view(), name="listar_criar_habito"),
    path('agenda/<int:pk>/', HabitoDetailView.as_view(), name = "deletar_habito"),
]