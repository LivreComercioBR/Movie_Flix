from django.urls import path
from .views import Homefilmes, DetalhesFilme, PesquisarFilme

app_name = 'filme_app'

urlpatterns = [
    #  filme/
    path('homefilmes/', Homefilmes.as_view(), name='homefilmes'),
    path('detalhes_filme/<int:pk>/',
         DetalhesFilme.as_view(), name='detalhes_filme'),
    path('pesquisarfilme/', PesquisarFilme.as_view(), name='pesquisarfilme')
]
