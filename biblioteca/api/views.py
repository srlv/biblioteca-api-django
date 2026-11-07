from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from biblioteca.models import Autor, Livro
from biblioteca.api.serializers import AutorSerializer, LivroSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [AllowAny]


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [AllowAny]