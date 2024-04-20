from django.urls import path
from .views import Homepage

app_name = 'movie_app'

urlpatterns = [
    path('homepage/', Homepage.as_view(), name='homepage'),
]
