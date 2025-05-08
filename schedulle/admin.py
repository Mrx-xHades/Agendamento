from django.contrib import admin
from schedulle.models import Cliente, Servico, Barbeiro


class barbeiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email' )
    search_fields = ('nome', )


class clienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email' )
    search_fields = ('nome', )


class servicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco' )
    search_fields = ('nome', )



admin.site.register(Barbeiro, barbeiroAdmin)
admin.site.register(Cliente, clienteAdmin)
admin.site.register(Servico, servicoAdmin)
