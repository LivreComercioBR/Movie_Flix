from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class HomepageForm(forms.Form):
    email = forms.EmailField(label=False)


class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# class EditarPerfil(UserCreationForm):
#     username = forms.CharField()
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ('username', 'email')
