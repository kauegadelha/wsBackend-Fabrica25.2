from rest_framework import viewsets
from .serializers import GeneroSerializer, AnimeSerializer
from .models import Genero, Anime
import requests

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

    def perform_create(self, serializer):
        titulo_enviado = serializer.validated_data['titulo']

        # Cria o anime com os dados do usuário
        anime = serializer.save()

        try: 
            response = requests.get(f'https://api.jikan.moe/v4/anime?q={titulo_enviado}')

            if response.status_code == 200 and response.json().get('data'):
                    anime_info = response.json()['data'][0]

                    # Atualiza apenas os campos complementares
                    anime.sinopse = anime_info.get('synopsis', '')
                    anime.data_lancamento = anime_info.get('aired', {}).get('from', None)
                    anime.save()

        except requests.RequestException:
            # Se a requisição falhar, mantém apenas os dados do usuário
            pass
    