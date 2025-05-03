from django.contrib import admin
from schedulle.models import Cliente, Servico


class clienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email' )
    search_fields = ('nome', )


class servicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco' )
    search_fields = ('nome', )




admin.site.register(Cliente, clienteAdmin)
admin.site.register(Servico, servicoAdmin)
