from django.urls import path
from pizzaria.views import ViewHome, ViewPedido



urlpatterns = [
    path('', ViewHome.as_view(), name="home"),
    path('', ViewPedido.as_view(), name="pedido"),
]
