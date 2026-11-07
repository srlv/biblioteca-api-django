from django.utils import timezone
from rest_framework import serializers
from biblioteca.models import Autor, Livro


class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = ["id", "nome", "nacionalidade", "data_nascimento"]


class LivroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Livro
        fields = ["id", "titulo", "descricao", "ano_publicacao", "autor"]

    def validate_ano_publicacao(self, value):
        ano_atual = timezone.localdate().year

        if value > ano_atual:
            raise serializers.ValidationError(
                "O ano de publicação não pode ser maior que o ano atual."
            )

        return value