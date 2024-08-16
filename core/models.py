from django.db import models
from django.utils import timezone


class Pizza(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    ingredientes = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to='pizzas/', blank=True, null=True)

    data_alteracao = models.DateTimeField(default=timezone.now)
    pizza_ativa = models.BooleanField(default=1,  blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Feedback(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='feedback')
    avaliacao = models.IntegerField()

    def __str__(self):
        return f"{self.pizza.nome} - {self.avaliacao} Stars"