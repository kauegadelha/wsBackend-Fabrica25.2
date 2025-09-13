from django.contrib import admin
from .models import Genero, Anime

class GeneroAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_editable = ['nome']

class AnimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data_lancamento']
    list_editable = ['titulo', 'data_lancamento']

admin.site.register(Genero, GeneroAdmin)
admin.site.register(Anime, AnimeAdmin)
