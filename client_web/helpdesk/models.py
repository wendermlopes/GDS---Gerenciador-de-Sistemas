# helpdesk/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Modelo para representar um Chamado de Helpdesk
class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Aberto'),
        ('In Progress', 'Em Progresso'),
        ('Closed', 'Fechado'),
        ('Resolved', 'Resolvido'),
        ('Waiting for User', 'Aguardando Usuário'),
    ]

    # === ADICIONADO: Opções para o campo de Categoria ===
    CATEGORY_CHOICES = [
        ('', '--- Selecione ---'), # Opção padrão vazia
        ('Hardware', 'Hardware'),
        ('Software', 'Software'),
        ('Rede', 'Rede'),
        ('E-mail', 'E-mail'),
        ('Outro', 'Outro'),
    ]

    # === ADICIONADO: Opções para o campo de Prioridade ===
    PRIORITY_CHOICES = [
        ('Low', 'Baixa'),
        ('Medium', 'Média'),
        ('High', 'Alta'),
        ('Urgent', 'Urgente'), # Mudado para 'Urgent' para consistência interna, mas o label é 'Urgente'
    ]


    subject = models.CharField(max_length=255, verbose_name="Assunto")
    description = models.TextField(verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_created', verbose_name="Criado por")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open', verbose_name="Status")

    # === ADICIONADO: Campo de Categoria ===
    # Definido como CharField com choices e verbose_name
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, verbose_name="Categoria") # Tornando Categoria OBRIGATÓRIA no modelo

    # === ADICIONADO: Campo de Prioridade ===
    # Definido como CharField com choices e um valor padrão, se desejar
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Medium', verbose_name="Prioridade") # Definindo padrão como Média

    # --- Campos Opcionais Comuns (Anexo será tratado depois) ---
    # assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tickets_assigned', verbose_name="Atribuído a")
    # updated_at = models.DateTimeField(auto_now=True, verbose_name="Última atualização em")
    # file_attachment = models.FileField(upload_to='helpdesk/attachments/', null=True, blank=True, verbose_name="Anexo")


    class Meta:
        verbose_name = "Chamado de Helpdesk"
        verbose_name_plural = "Chamados de Helpdesk"
        ordering = ['-created_at']

    def __str__(self):
        return f"Chamado #{self.id} ({self.status}): {self.subject}"