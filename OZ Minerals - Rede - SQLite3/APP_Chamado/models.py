from django.db import models
from django.contrib.auth.models import User

#####################################################################################################################################################################################

# Defina suas escolhas de títulos de chamados aqui
CHOICE_TITULO_CHAMADOS = [
    ('Instalação de Software', 'Instalação de Software'),
    ('Manutenção em Desktop', 'Manutenção em Desktop'),
    ('Upgrade de Software', 'Upgrade de Software'),
    ('Ativar Ponto de Rede', 'Ativar Ponto de Rede'),
    ('Outros', 'Outros'),
]

CHOICE_GERENTES_CHAMADOS = [
    ('Lucas Fayad', 'Lucas Fayad'),
    ('Manoel Lucas', 'Manoel Lucas'),
    ('Lucas Tarias', 'Lucas Tarias'),
    ('Angelo Pickler', 'Angelo Pickler'),
]

CHOICE_DEPARTAMENTO_CHAMADOS = [
    ('Planta', 'Planta'),
    ('Administrativo', 'Administrativo'),
    ('Recusros Humanos', 'Recusros Humanos'),
    ('Armazén', 'Armazén'),
]

class Chamado(models.Model):
    ticket = models.CharField('Ticket', max_length=20, unique=True, editable=False)
    tipodechamado = models.CharField('Tipo de Chamado', max_length=40, choices=CHOICE_TITULO_CHAMADOS)
    departamento = models.CharField('Departamento', max_length=40, choices=CHOICE_DEPARTAMENTO_CHAMADOS)
    gerentes = models.CharField('Gerente', max_length=40, choices=CHOICE_GERENTES_CHAMADOS)
    descricao = models.TextField('Descrição')
    status = models.CharField('Status',
        max_length=20,
        choices=[
            ('aberto', 'Aberto'),
            ('em andamento', 'Em andamento'),
            ('resolvido', 'Resolvido'),
            ('fechado', 'Fechado'),
        ],
        default='aberto'
    )
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='chamados/', blank=True, null=True)

    def __str__(self):
        return f'{self.ticket} - {self.titulo}'

    def save(self, *args, **kwargs):
        if not self.ticket:
            last_ticket = Chamado.objects.all().order_by('id').last()
            if not last_ticket:
                self.ticket = 'Ticket-000001'
            else:
                ticket_number = int(last_ticket.ticket.split('-')[1]) + 1
                self.ticket = f'Ticket-{ticket_number:06d}'
        super().save(*args, **kwargs)

#####################################################################################################################################################################################