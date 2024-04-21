from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Filme
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class Homefilmes(LoginRequiredMixin, ListView):
    # O objetivo desta classe é exibir uma lista de objetos.
    template_name = 'homefilmes.html'
    model = Filme
    # ela vai me passar um contexto em forma de object_list


class DetalhesFilme(LoginRequiredMixin, DetailView):
    template_name = 'detalhes_filme.html'
    model = Filme

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # preciso descobrir qual filme o usuário está acessando
        filme = self.get_object()
        # preciso somar 1 visualização àquele filme
        filme.visualizacoes += 1
        # agora preciso salvar a alteração no banco de dados
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)

        return super().get(request, *args, **kwargs)
        # aqui ele redireciona o usuário para a url final

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(DetalhesFilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(
            categoria=self.get_object().categoria)[0:5]
        # no HTML o filme é chamado de object e aqui na views é chamado de get_object. Então, get_objet().categoria

        context["filmes_relacionados"] = filmes_relacionados
        return context

    # Esta classe ao contrário da listview ela me passa somente um object. Funciona como na função get_object.


class PesquisarFilme(LoginRequiredMixin, ListView):
    template_name = 'pesquisarfilme.html'
    model = Filme

    def get_queryset(self) -> QuerySet[Any]:
        termo_pesquisa = self.request.GET.get("query")
        if termo_pesquisa:
            object_list = self.model.objects.filter(
                titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None
