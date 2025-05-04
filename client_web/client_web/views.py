# client_web/views.py
from django.shortcuts import render # Importa a função render para carregar templates
from django.contrib.auth.decorators import login_required # Importa o decorator para exigir login

# Usa o decorator @login_required para garantir que esta view só possa ser acessada por usuários autenticados.
# Se um usuário não logado tentar acessar esta URL, o Django automaticamente o redirecionará para a URL de login
# definida em settings.py (LOGIN_URL) ou nas URLs de autenticação.
@login_required
def home_view(request):
    """
    Função de view para a página inicial / dashboard do usuário.
    Exige que o usuário esteja autenticado para acessar.
    """
    # A função render carrega o template especificado ('home.html')
    # e passa o objeto 'request' para ele, que inclui o usuário autenticado.
    # O objeto 'user' fica disponível no template home.html graças ao middleware de autenticação do Django
    # e ao decorator @login_required.
    return render(request, 'home.html')

# Nota: Outras views para diferentes funcionalidades (como gerenciar clientes, produtos, etc.)
# serão adicionadas a este arquivo no futuro, e também serão protegidas por @login_required
# ou verificações de permissão, dependendo do caso.