from rest_framework import serializers
from .models import Anime, Genero

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nome']

class AnimeSerializer(serializers.ModelSerializer):
    # Mostra nomes dos gêneros na resposta
    generos = GeneroSerializer(many=True, read_only=True)

    generos_nomes = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Anime
        fields = ['id', 'titulo', 'sinopse', 'data_lancamento', 'generos', 'generos_nomes']

    def create(self, validated_data):
        generos_nomes = validated_data.pop('generos_nomes', [])
        anime = Anime.objects.create(**validated_data)

        for nome in generos_nomes:
            genero, created = Genero.objects.get_or_create(nome=nome)
            anime.generos.add(genero)

        return anime

    