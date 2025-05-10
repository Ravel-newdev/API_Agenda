from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Habito
from . serializers import HabitoSerializer

class HabitoView(APIView):
    def get(self, request):
        agenda_de_habitos = Habito.objects.all()
        serializer = HabitoSerializer(agenda_de_habitos, many=True)
        print("[GET] Listando hábitos")
        return Response(serializer.data)
    def post(self, request):
        serializer = HabitoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(f"[POST] Hábito criado: {serializer.data}")
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        print(f"[POST] Erro a criar o novo hábito:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HabitoDetailView(APIView):
    def delete(self, request, pk):
        try:
            habito = Habito.objects.get(pk=pk)
            habito.delete()
            print(f"[DELETE]  Hábito com ID {pk} removido.")
            #return Response({"mensagem": f'Hábito {pk} removido sem erros.'}, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Habito.DoesNotExist:
            print(f"[DELETE] Hábito com o ID {pk} não encontrado.")
            return Response({'erro': 'Hábito não encontrado'}, status=status.HTTP_404_NOT_FOUND)

#testes automatizados genericos
class listar_criar_habito(generics.ListCreateAPIView):
    queryset = Habito.objects.all()
    serializer_class = HabitoSerializer

class deletar_habito(generics.DestroyAPIView):
    queryset = Habito.objects.all()
    serializer_class = HabitoSerializer
