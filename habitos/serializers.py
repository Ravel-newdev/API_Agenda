from rest_framework import serializers
from .models import Habito

class HabitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habito
        fields = ['id', 'nome', 'frequencia', 'desc', 'status', 'criacao']