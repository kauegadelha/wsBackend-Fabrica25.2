from rest_framework import viewsets
from .serializers import GeneroSerializer, AnimeSerializer
from .models import Genero, Anime
from dateutil.parser import parse
from rest_framework.exceptions import ValidationError
import requests

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

    def perform_create(self, serializer):
        titulo_enviado = serializer.validated_data['titulo']
        # IDs dos gêneros selecionados pelo usuário para associar ao anime
        generos_ids = serializer.validated_data.pop('generos_ids', [])

        try: 
            response = requests.get(f'https://api.jikan.moe/v4/anime?q={titulo_enviado}',
                                    timeout=5)

            if response.status_code == 200 and response.json().get('data'):
                    anime_info = response.json()['data'][0]

                    if anime_info['title'].strip().lower() != titulo_enviado.strip().lower():
                        raise ValidationError({'titulo': 'Anime não encontrado na Jikan API. Não foi possível salvar.'})

                    # salva no banco
                    anime = serializer.save()

                    if generos_ids:
                         # Associa os gêneros selecionados ao anime recém-criado
                         anime.generos.set(generos_ids)

                    # Atualiza apenas os campos complementares
                    anime.sinopse = anime_info.get('synopsis', '')
                    data_str = anime_info.get('aired', {}).get('from', None)
                    if data_str:
                         # Converte para Ano-Mês-Dia
                         anime.data_lancamento = parse(data_str).date().isoformat()
                    else:
                         anime.data_lancamento = ""
                    anime.save()

        except requests.RequestException:
            # Se a requisição falhar
            raise ValidationError({'erro': 'Não foi possível consultar a Jikan API no momento.'})
    