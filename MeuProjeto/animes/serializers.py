from rest_framework import serializers
from .models import Anime, Genero

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nome']

class AnimeSerializer(serializers.ModelSerializer):
    # Mostra nomes dos gêneros na resposta
    generos = GeneroSerializer(many=True, read_only=True)

    # Campo para receber os IDs dos gêneros no POST/PUT/PATCH
    generos_ids = serializers.PrimaryKeyRelatedField(
        many = True, 
        queryset = Genero.objects.all(),
        write_only = True,
        required = False,
        source = "generos" # aponta para o campo ManyToMany do modelo
    )

    class Meta:
        model = Anime
        fields = ['id', 'titulo', 'sinopse', 'data_lancamento', 'generos', 'generos_ids']
        

    