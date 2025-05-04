# users/views.py
from django.shortcuts import render # Já existe no seu arquivo
# from django.http import HttpResponse # Se precisar para outras views neste arquivo

# Importa a View de Login embutida do Django
from django.contrib.auth.views import LoginView

# Importa o nosso formulário de autenticação customizado que criamos em users/forms.py
from .forms import CustomAuthenticationForm

# Importa as configurações do projeto para usar SESSION_COOKIE_AGE (para "Lembre-me")
from django.conf import settings

# === Classe da View de Login Customizada ===
# Esta View herda da LoginView do Django e adiciona a lógica para "Lembre-me".
class CustomLoginView(LoginView):
    """
    View de Login customizada que usa nosso formulário customizado (CustomAuthenticationForm)
    e implementa a lógica para a opção "Lembre-me".
    """
    # Define qual template HTML esta View deve usar para exibir a página de login
    # Aponta para o arquivo que já criamos em client_web/templates/registration/
    template_name = 'registration/login.html'

    # Define qual formulário esta View deve usar para processar a entrada do usuário.
    # Apontamos para o nosso formulário customizado com o campo 'remember_me' e rótulos traduzidos.
    authentication_form = CustomAuthenticationForm

    # LOGIN_REDIRECT_URL é definido em settings.py (nós a configuramos como '/')
    # e esta View usará essa configuração por padrão para onde redirecionar após um login bem-sucedido.


    def form_valid(self, form):
        """
        Este método é chamado quando o formulário é submetido e a validação (incluindo a autenticação do usuário) é bem-sucedida.
        Nós o sobrescrevemos para controlar a duração da sessão com base no valor do checkbox "Lembre-me".
        """
        # === PASSO 1: Chamar o método form_valid da classe pai (LoginView) ===
        # Este passo é CRUCIAL. É aqui que a autenticação real acontece (o usuário é colocado na sessão)
        # e a View base prepara a resposta (geralmente um redirecionamento).
        response = super().form_valid(form)

        # === PASSO 2: Lógica para "Lembre-me" ===
        # Acessamos os dados limpos do formulário para ver se o checkbox 'remember_me' foi marcado.
        if form.cleaned_data.get('remember_me'):
            # Se 'remember_me' estiver marcado (True), definimos a sessão para expirar
            # de acordo com a configuração SESSION_COOKIE_AGE em settings.py.
            # set_expiry(None) significa "usar o tempo de expiração global".
            # O padrão SESSION_COOKIE_AGE é 2 semanas.
            self.request.session.set_expiry(settings.SESSION_COOKIE_AGE)
        else:
            # Se 'remember_me' NÃO estiver marcado (False), queremos que a sessão expire
            # automaticamente quando o usuário fechar o navegador.
            # set_expiry(0) significa "expirar ao fechar o navegador".
            self.request.session.set_expiry(0)
        # === Fim da Lógica para "Lembre-me" ===

        # === PASSO 3: Retornar a resposta ===
        # Retornamos a resposta que foi preparada pelo método form_valid da classe pai.
        # Esta resposta é geralmente um redirecionamento para a página definida por LOGIN_REDIRECT_URL.
        return response

# === Fim da Classe CustomLoginView ===


# Você pode adicionar outras Views para o app users aqui, se precisar (ex: cadastro, perfil, etc.)
# def user_profile_view(request):
#     pass # Exemplo de outra view