from django.urls import path, include
from .views import HabitoView, HabitoDetailView

urlpatterns = [
    path('agenda/',HabitoView.as_view()),
    path('agenda/<int:pk>/', HabitoDetailView.as_view()),
]