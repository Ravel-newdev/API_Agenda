from django.db import models

# Create your models here.

class Habito(models.Model):
    nome = models.CharField(max_length=100)
    frequencia = models.CharField(max_length=50, default="Todo dia")
    def __str__(self):
        return f'{self.nome} ({self.frequencia})'