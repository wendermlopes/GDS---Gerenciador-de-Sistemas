# helpdesk/forms.py
from django import forms
from .models import Ticket # Importa o modelo Ticket

# Cria um formulário baseado no modelo Ticket
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket # Indica que este formulário está baseado no modelo Ticket
        # Define quais campos do modelo Ticket devem ser incluídos no formulário
        # === MODIFICADO: Adicionados 'category' e 'priority' à lista de campos ===
        fields = ['subject', 'category', 'priority', 'description'] # Inclui Assunto, Categoria, Prioridade e Descrição

        # Opcional: Você pode adicionar 'labels' e 'widgets' personalizados aqui se quiser
        # widgets = {
        #     'description': forms.Textarea(attrs={'rows': 4}),
        #     'category': forms.Select(attrs={'class': 'form-control'}), # Exemplo de adição de classe CSS
        # }
        # labels = {
        #     'subject': 'Assunto do Chamado',
        #     'category': 'Selecione a Categoria',
        # }

    # Opcional: Você pode adicionar validações customizadas ou métodos aqui
    # def clean_subject(self):
    #     subject = self.cleaned_data.get('subject')
    #     if len(subject) < 5:
    #         raise forms.ValidationError("O assunto deve ter pelo menos 5 caracteres.")
    #     return subject