# users/forms.py
from django.contrib.auth.forms import AuthenticationForm
from django import forms
# Importar gettext_lazy para permitir tradução futura dos rótulos - ADICIONADO
from django.utils.translation import gettext_lazy as _

class CustomAuthenticationForm(AuthenticationForm):
    """
    Formulário de autenticação customizado para traduzir rótulos e adicionar "Lembre-me".
    """
    username = forms.CharField(
        # Usando _() para marcar o rótulo para potencial tradução futura - MODIFICADO
        label=_("Nome de Usuário"),
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        # Usando _() para marcar o rótulo para potencial tradução futura - MODIFICADO
        label=_("Senha"),
        strip=False,
        widget=forms.PasswordInput
    )
    # Adiciona o campo "Lembre-me" (um checkbox) - ADICIONADO
    remember_me = forms.BooleanField(
        label=_("Lembre-me"), # Rótulo em português para o checkbox
        required=False, # O campo não é obrigatório (o usuário pode optar por não marcar)
        widget=forms.CheckboxInput # Usa o widget de checkbox padrão
    )

    # O restante da lógica de validação do formulário é herdado da classe pai (AuthenticationForm).
    # A lógica de como usar o valor de 'remember_me' para a sessão será na View.