from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


campos = list(UserAdmin.fieldsets)
campos.append(("Histórico", {'fields': ('filmes_vistos', )}))

UserAdmin.fieldsets = tuple(campos)


admin.site.register(User, UserAdmin)
