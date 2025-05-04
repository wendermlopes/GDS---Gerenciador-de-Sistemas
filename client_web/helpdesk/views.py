# helpdesk/views.py
from django.shortcuts import render, redirect # Importamos redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages # Importamos o módulo messages do Django

# Importamos o modelo Ticket e o formulário TicketForm que criamos
from .models import Ticket
from .forms import TicketForm # === ADICIONADO: Importamos TicketForm ===


# View para exibir o formulário de criação de novo chamado e processar a submissão
# Protegida por @login_required: só usuários logados podem acessar
@login_required
def create_ticket_view(request):
    """
    View para exibir o formulário de criação de um novo chamado de helpdesk
    e processar a submissão do formulário.
    """
    if request.method == 'POST':
        # === Lógica para lidar com a submissão do formulário (requisição POST) ===
        # Criamos uma instância do formulário com os dados enviados na requisição POST
        form = TicketForm(request.POST)
        # Verificamos se os dados do formulário são válidos (ex: campos obrigatórios preenchidos, tipos corretos)
        if form.is_valid():
            # Salvamos o formulário, mas NÃO commitamos ainda no banco de dados (commit=False).
            # Fazemos isso porque precisamos adicionar o usuário que criou o chamado (request.user)
            # antes de salvar o objeto Ticket completo no banco.
            ticket = form.save(commit=False)
            # Definimos o campo 'created_by' do objeto ticket para o usuário logado atualmente
            ticket.created_by = request.user
            # Agora que o campo 'created_by' está definido, podemos salvar a instância completa no banco de dados
            ticket.save()

            # Adicionamos uma mensagem de sucesso que será exibida ao usuário na próxima página
            # Certifique-se que o framework de mensagens está configurado em settings.py (geralmente é por padrão)
            messages.success(request, 'Seu chamado foi aberto com sucesso!')

            # Redirecionamos o usuário para a página de listagem de chamados após a criação bem-sucedida.
            # 'list_tickets' é o nome da URL definida em helpdesk/urls.py
            # Como helpdesk/urls.py está incluído sob o prefixo 'helpdesk/' nas URLs principais,
            # o Django resolverá 'list_tickets' para '/helpdesk/list/'.
            return redirect('list_tickets') # === MODIFICADO: Redireciona após sucesso ===

    else: # === Lógica para exibir o formulário (requisição GET) ===
        # Se a requisição não for POST (geralmente é GET quando a página é acessada pela primeira vez),
        # criamos uma instância vazia do formulário para ser exibida.
        form = TicketForm()

    # Em caso de requisição GET ou se o formulário POST for inválido, renderizamos o template
    # 'helpdesk/create_ticket.html'. Passamos a instância do formulário ('form') para o template
    # para que ele possa exibir os campos do formulário (e quaisquer erros, se o formulário for inválido).
    return render(request, 'helpdesk/create_ticket.html', {'form': form}) # === MODIFICADO: Renderiza template com formulário ===


# View para exibir a lista de chamados
@login_required
def list_tickets_view(request):
    """
    View para exibir uma lista de chamados de helpdesk.
    (Esta view será atualizada depois para buscar e exibir chamados reais)
    """
    # Placeholder: Retorna uma resposta HTTP simples por enquanto
    return HttpResponse("<h1>Lista de Chamados</h1><p>A lista de chamados de helpdesk virá aqui em breve.</p>")

    # --- Lógica futura para buscar chamados e renderizar template ---
    # tickets = Ticket.objects.filter(created_by=request.user).order_by('-created_at') # Ex: apenas chamados do usuário logado
    # return render(request, 'helpdesk/list_tickets.html', {'tickets': tickets})