from rest_framework import viewsets
from .serializers import GeneroSerializer, AnimeSerializer
from .models import Genero, Anime
from dateutil.parser import parse
import requests

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

    def perform_create(self, serializer):
        titulo_enviado = serializer.validated_data['titulo']
        generos_ids = serializer.validated_data.pop('generos_ids', [])

        # Cria o anime com os dados do usuário
        anime = serializer.save()

        if generos_ids:
             anime.generos.set(generos_ids)

        try: 
            response = requests.get(f'https://api.jikan.moe/v4/anime?q={titulo_enviado}')

            if response.status_code == 200 and response.json().get('data'):
                    anime_info = response.json()['data'][0]

                    # Atualiza apenas os campos complementares
                    anime.sinopse = anime_info.get('synopsis', '')
                    data_str = anime_info.get('aired', {}).get('from', None)
                    if data_str:
                         #Converte para Ano-Mês-Dia
                         anime.data_lancamento = parse(data_str).date().isoformat()
                    else:
                         anime.data_lancamento = ""
                    anime.save()

        except requests.RequestException:
            # Se a requisição falhar, mantém apenas os dados do usuário
            pass
    