from django.db import models


LISTA_CATEGORIAS = (
    ('ANALISES', 'Analises'),
    ('PROGRAMACAO', 'Programacao'),
    ('APRESENTACAO', 'Apresentacao'),
    ('OUTROS', 'Outros'),
)


class Filme(models.Model):
    titulo = models.CharField(max_length=150, unique=True)
    thumb = models.ImageField(upload_to='thumbs_filmes')
    descricao = models.TextField(max_length=1000, blank=True, null=True)
    categoria = models.CharField(
        max_length=32, choices=LISTA_CATEGORIAS, blank=True, null=True)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class Episodios(models.Model):
    filme = models.ForeignKey(
        Filme, on_delete=models.CASCADE, related_name='epsodios', blank=True, default='')
    nome = models.CharField(
        max_length=150, unique=True, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nome
