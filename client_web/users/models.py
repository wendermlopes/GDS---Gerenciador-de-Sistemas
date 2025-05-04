# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Define as opções para o campo 'role'
    ROLE_CHOICES = [
        ('cliente', 'Cliente'),
        ('admin', 'Administrador'),
        ('super_admin', 'Super Administrador'),
    ]
    # Adiciona o campo 'role' ao modelo de usuário
    # max_length deve ser suficiente para o maior cargo ('super_admin')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='cliente')

    # Adiciona related_name para evitar conflitos com o modelo de usuário padrão do Django
    # (Boa prática ao herdar de AbstractUser)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",
        related_query_name="user",
    )


    def __str__(self):
        # Representação em string do objeto CustomUser (útil no admin site)
        return self.username

    # Você pode adicionar métodos customizados aqui se precisar de lógica específica baseada na role
    # Exemplo:
    # @property
    # def is_cliente(self):
    #     return self.role == 'cliente'

    # @property
    # def is_admin_ou_super_admin(self):
    #     return self.role in ['admin', 'super_admin']


# Lembre-se de que o modelo CustomUser deve ser referenciado em settings.py