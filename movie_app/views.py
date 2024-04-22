from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, FormView, UpdateView
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaForm, HomepageForm
from .models import User


class Homepage(FormView):
    template_name = 'homepage.html'
    form_class = HomepageForm

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('filme_app:homefilmes')
        else:
            # retorna o usuário para a classe final da view, no caso homepage
            return super().get(request, *args, **kwargs)

    def get_success_url(self) -> str:
        email = self.request.POST.get("email")
        # Verificar se o usuário está cadastro
        usuario = User.objects.filter(email=email)
        if usuario:
            return reverse('movie_app:login')
        else:
            return reverse('movie_app:criarconta')


class CriarConta(FormView):
    template_name = 'criarconta.html'
    # precisei importar o form personalizado que criei e importar o FormView do django
    form_class = CriarContaForm

    def form_valid(self, form: Any) -> HttpResponse:
        form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        # esta função ESPERA UM LINK como resposta e NÃO uma função de redirecionamento, como por exemplo o redirect.
        return reverse('movie_app:login')


def logout(request):
    auth.logout(request)
    return redirect('movie_app:login')


class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = User
    fields = ('username', 'email')

    def get_success_url(self) -> str:
        return reverse('filme_app:homefilmes')
