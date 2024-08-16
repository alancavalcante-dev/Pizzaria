from django.shortcuts import render
from django.views import View
from core.models import Pizza
from django.db.models import Avg, Count



class ViewHome(View):
 
    def get(self, request):
        ranking = Pizza.objects.annotate(
                avg_rating=Avg('feedback__avaliacao'),  
                num_reviews=Count('feedback__avaliacao')
            ).order_by('-avg_rating', '-num_reviews')[:3]  # Ordene pelas avaliações médias e número de avaliações
        

        return render(
            request,
            'pizzaria/home.html',
            {'ranking_pizzas': ranking}
        )

class ViewPedido(View):

    def get(self, request):
        return render(
            request,
            'pizzaria/pedido.html'
        )