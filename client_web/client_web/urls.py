# Gerenciamento/urls.py
from django.contrib import admin
from django.urls import path, include # === Certifique-se que include está importado ===

# Importa as views dos nossos aplicativos
from client_web import views as project_views # Views do aplicativo client_web
from users.views import CustomLoginView # View de login customizada do app users
# Não precisamos importar as views do helpdesk aqui diretamente, apenas incluir suas urls

# Importa as views de autenticação embutidas do Django
from django.contrib.auth import views as auth_views


urlpatterns = [
    # URLs para o painel de administração do Django
    path('admin/', admin.site.urls),

    # URLs de autenticação (login, logout, etc.) - Usando a customizada e a embutida
    path('accounts/login/',
         CustomLoginView.as_view(),
         name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(next_page='home'), # Redireciona para 'home' após logout
         name='logout'),

    # URLs para o fluxo de Reset de Senha do Django
    path('accounts/password_reset/',
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset'),
    path('accounts/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('accounts/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

    # URL para a página inicial (Dashboard)
    path('', project_views.home_view, name='home'),

    # === ADICIONADO: Inclui as URLs do aplicativo helpdesk ===
    # Todas as URLs definidas em helpdesk/urls.py serão acessíveis sob o prefixo /helpdesk/
    path('helpdesk/', include('helpdesk.urls')), # Ex: /helpdesk/new/, /helpdesk/list/
]