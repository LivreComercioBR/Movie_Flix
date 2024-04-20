from django.shortcuts import render
from django.views.generic import TemplateView


# def homepage(request):
#     return render(request, 'homepage.html')


class Homepage(TemplateView):
    template_name = 'homepage.html'
