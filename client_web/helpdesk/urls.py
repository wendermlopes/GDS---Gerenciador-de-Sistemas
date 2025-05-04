# helpdesk/urls.py
from django.urls import path # Importa a função path
from . import views # Importa as views do mesmo diretório (o aplicativo helpdesk)

urlpatterns = [
    # Define a URL para criar um novo chamado. Nome: 'create_ticket'. View: views.create_ticket_view
    # O caminho será '/helpdesk/new/' quando incluído nas URLs principais
    path('new/', views.create_ticket_view, name='create_ticket'),

    # Define a URL para listar os chamados. Nome: 'list_tickets'. View: views.list_tickets_view
    # O caminho será '/helpdesk/list/' quando incluído nas URLs principais
    path('list/', views.list_tickets_view, name='list_tickets'),

    # --- URLs para funcionalidades futuras (descomente quando implementar) ---
    # path('<int:pk>/', views.ticket_detail_view, name='ticket_detail'), # Ver detalhes de um chamado específico
    # path('<int:pk>/edit/', views.update_ticket_view, name='update_ticket'), # Editar um chamado
    # path('<int:pk>/delete/', views.delete_ticket_view, name='delete_ticket'), # Deletar um chamado
]