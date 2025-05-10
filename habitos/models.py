from django.db import models

# Create your models here.

class Habito(models.Model):
    nome = models.CharField(max_length=100)
    frequencia = models.CharField(max_length=50, default="Todo dia")
    desc = models.TextField(blank=True, default="")
    status = models.CharField(max_length=20, default="ativo")
    criacao = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.nome} {self.frequencia} {self.desc} {self.status} {self.criacao}'