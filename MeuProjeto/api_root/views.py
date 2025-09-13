#views customizada para o caminho do admin na api do projeto
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse

@api_view(['GET'])
def custom_api_root(request, format = None):
    return Response({
        'generos': request.build_absolute_uri(reverse('genero-list')),
        'animes': request.build_absolute_uri(reverse('anime-list')),
        'admin': request.build_absolute_uri('/admin/')
    })