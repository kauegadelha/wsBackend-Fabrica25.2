from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Anime(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    imagem = models.URLField(blank=True)
    tipo = models.CharField(max_length=50)  # Exemplo: TV, Movie, OVA
    episodios = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True)
    nota = models.FloatField(blank=True, null=True)

    generos = models.ManyToManyField(Genero, related_name='animes')

    def __str__(self):
        return self.titulo