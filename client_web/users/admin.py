# users/admin.py
from django.contrib import admin
from .models import CustomUser # Importa o seu modelo de usuário customizado

# Registra o seu modelo CustomUser no painel de administração do Django
admin.site.register(CustomUser)

# Você pode adicionar mais configurações aqui no futuro para customizar
# como o modelo é exibido no admin (filtros, campos visíveis, etc.)
# Ex: from django.contrib.auth.admin import UserAdmin
# class CustomUserAdmin(UserAdmin):
#     # Adicione 'role' aos campos que são exibidos/editáveis
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('role',)}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('role',)}),
#     )
# admin.site.register(CustomUser, CustomUserAdmin)