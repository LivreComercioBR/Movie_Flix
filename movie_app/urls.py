from django.urls import path, reverse_lazy
from .views import Homepage, CriarConta, EditarPerfil
from django.contrib.auth import views as auth_views
from .import views as logoutview

app_name = 'movie_app'

urlpatterns = [
    path('homepage/', Homepage.as_view(), name='homepage'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logoutview.logout, name='logout'),
    path('criarconta/', CriarConta.as_view(), name='criarconta'),
    path('editarperfil/<int:pk>/',
         EditarPerfil.as_view(), name='editarperfil'),
    path('mudarsenha/', auth_views.PasswordChangeView.as_view(template_name='editarperfil.html',
         success_url=reverse_lazy('filme_app.homefilmes')), name='mudarsenha'),
]
