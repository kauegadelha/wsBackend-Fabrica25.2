from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Anime, Genero
from .serializers import AnimeSerializer, GeneroSerializer
import requests

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

    @action(detail=False, methods=['get'])
    def buscar_api_externa(self, request):
        url = "https://api.jikan.moe/v4/top/anime"  # coloque a URL correta
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            top_animes = dados.get('data', [])[:10]  # pega só os 10 primeiros
            return Response(top_animes)
        else:
            return Response({"erro": "Não foi possível obter os dados"}, status=500)
