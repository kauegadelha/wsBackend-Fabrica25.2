from rest_framework import serializers
from .models import Anime, Genero

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nome']

class AnimeSerializer(serializers.ModelSerializer):
    generos = GeneroSerializer(many=True, read_only=True)  # Mostrar detalhes dos generos
    generos_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genero.objects.all(),
        source='generos',  # indica que está relacionado ao campo generos do modelo
        write_only=True    # esse campo só é usado para entrada, não aparece na resposta
    )

    class Meta:
        model = Anime
        fields = ['id', 'titulo', 'descricao', 'imagem', 'tipo', 'episodios', 'status', 'nota', 'generos', 'generos_ids']

