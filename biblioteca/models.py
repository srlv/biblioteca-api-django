from django.db import models

from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=150)
    nacionalidade = models.CharField(max_length=100, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    ano_publicacao = models.PositiveSmallIntegerField()
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name="livros"
    )

    def __str__(self):
        return self.titulo