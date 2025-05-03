from django.shortcuts import render, get_object_or_404 , redirect
from django.views.generic import ListView
from .models import Agendamento
from django.http import HttpResponse
from .models import Cliente, Servico, Agendamento
from .forms import AgendamentoForm
from django.utils import timezone

class AgendamentoListView(ListView):
    model = Agendamento
    template_name = 'agendamentos/lista_agendamentos.html'
    context_object_name = 'agendamentos'

    def get_queryset(self):
        # Filtra apenas agendamentos futuros (se quiser mostrar apenas os agendamentos não concluídos)
        return Agendamento.objects.filter(data_hora__gte=timezone.now()).order_by('data_hora')



# views.py

def criar_agendamento(request):
    if request.method == "POST":
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm()

    return render(request, 'agendamentos/criar_agendamento.html', {'form': form})



def detalhar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    return render(request, 'agendamentos/detalhar_agendamento.html', {'agendamento': agendamento})

# views.py


def editar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)

    if request.method == "POST":
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('detalhar_agendamento', agendamento_id=agendamento.id)
    else:
        form = AgendamentoForm(instance=agendamento)

    return render(request, 'agendamentos/editar_agendamento.html', {'form': form})

# views.py
from django.shortcuts import redirect, get_object_or_404
from .models import Agendamento

def excluir_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    agendamento.delete()
    return redirect('lista_agendamentos')

