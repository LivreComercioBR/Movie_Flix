from .models import Filme


def lista_filmes_recentes(request):
    # para listar os 10 últimos filmes lançados
    filmes_recentes = Filme.objects.all().order_by("-data_criacao")[0:8]

    return {"lista_filmes_recentes": filmes_recentes}


def lista_filmes_emalta(request):
    # para listar os últimos 10 filmes lançadoss
    filmes_emalta = Filme.objects.all().order_by('-visualizacoes')[0:8]

    return {"lista_filmes_emalta": filmes_emalta}


def filme_destaque(request):
    destaque = Filme.objects.order_by('-data_criacao')[0]
    return {"filme_destaque": destaque}
