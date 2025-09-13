from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome
    
class Anime(models.Model):
    titulo = models.CharField(max_length=100)
    sinopse = models.TextField(blank=True)
    data_lancamento = models.CharField(max_length=20, blank=True)
    generos = models.ManyToManyField(Genero, related_name='animes')
    # você pode adicionar mais campos: imagem, nota, episodios, etc.

    def __str__(self):
        return self.titulo