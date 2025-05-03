from django.db import models
from django.utils import timezone

# Cliente do sistema de agendamentos
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome

# Tipo de Serviço disponível no cabeleireiro
class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

# Status do Agendamento
class StatusAgendamento(models.TextChoices):
    PENDENTE = 'P', 'Pendente'
    CONFIRMADO = 'C', 'Confirmado'
    CONCLUIDO = 'D', 'Concluído'
    CANCELADO = 'X', 'Cancelado'

# Agendamento de cabeleireiro
class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.SET_NULL, null=True)
    data_hora = models.DateTimeField()
    status = models.CharField(
        max_length=1,
        choices=StatusAgendamento.choices,
        default=StatusAgendamento.PENDENTE,
    )
    observacoes = models.TextField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Agendamento {self.id} - {self.cliente.nome} - {self.servico.nome} - {self.data_hora}"

    def is_agendamento_futuro(self):
        return self.data_hora > timezone.now()
