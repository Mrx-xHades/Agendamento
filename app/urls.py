from django.contrib import admin
from django.urls import path
from schedulle.views import AgendamentoListView, criar_agendamento, detalhar_agendamento, editar_agendamento, excluir_agendamento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AgendamentoListView.as_view(), name='lista_agendamentos'),
    path('agendamento/criar/', criar_agendamento, name='criar_agendamento'),
    path('agendamento/<int:agendamento_id>/', detalhar_agendamento, name='detalhar_agendamento'),
    path('agendamento/editar/<int:agendamento_id>/', editar_agendamento, name='editar_agendamento'),
    path('agendamento/excluir/<int:agendamento_id>/', excluir_agendamento, name='excluir_agendamento'),
]
