from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from biblioteca.models import Autor, Livro


class LivroAPITests(APITestCase):
    def setUp(self):
        self.autor = Autor.objects.create(
            nome="Machado de Assis",
            nacionalidade="Brasileira",
        )
        self.livro = Livro.objects.create(
            titulo="Dom Casmurro",
            descricao="Romance clássico",
            ano_publicacao=1899,
            autor=self.autor,
        )
        self.url_lista = reverse("livros-list")
        self.url_detalhe = reverse("livros-detail", args=[self.livro.id])

    def test_cadastrar_livro(self):
        dados = {
            "titulo": "Memórias Póstumas de Brás Cubas",
            "descricao": "",
            "ano_publicacao": 1881,
            "autor": self.autor.id,
        }
        resposta = self.client.post(self.url_lista, dados, format="json")

        self.assertEqual(resposta.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Livro.objects.count(), 2)

    def test_listar_livros(self):
        resposta = self.client.get(self.url_lista)

        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        dados = resposta.data
        # funciona com ou sem paginação
        itens = dados["results"] if isinstance(dados, dict) else dados
        self.assertEqual(len(itens), 1)

    def test_consultar_livro_por_id(self):
        resposta = self.client.get(self.url_detalhe)

        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.assertEqual(resposta.data["titulo"], "Dom Casmurro")

    def test_atualizar_livro(self):
        resposta = self.client.patch(
            self.url_detalhe, {"titulo": "Dom Casmurro - 2ª edição"}, format="json"
        )

        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.livro.refresh_from_db()
        self.assertEqual(self.livro.titulo, "Dom Casmurro - 2ª edição")

    def test_excluir_livro(self):
        resposta = self.client.delete(self.url_detalhe)

        self.assertEqual(resposta.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Livro.objects.count(), 0)

    def test_rejeita_ano_de_publicacao_no_futuro(self):
        dados = {
            "titulo": "Livro do Futuro",
            "descricao": "",
            "ano_publicacao": timezone.localdate().year + 1,
            "autor": self.autor.id,
        }
        resposta = self.client.post(self.url_lista, dados, format="json")

        self.assertEqual(resposta.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("ano_publicacao", resposta.data)
        self.assertEqual(Livro.objects.count(), 1)

    def test_aceita_ano_de_publicacao_atual(self):
        dados = {
            "titulo": "Lançamento do Ano",
            "descricao": "",
            "ano_publicacao": timezone.localdate().year,
            "autor": self.autor.id,
        }
        resposta = self.client.post(self.url_lista, dados, format="json")

        self.assertEqual(resposta.status_code, status.HTTP_201_CREATED)


class AutorAPITests(APITestCase):
    def test_cadastrar_autor(self):
        dados = {"nome": "Clarice Lispector", "nacionalidade": "Brasileira"}
        resposta = self.client.post(reverse("autores-list"), dados, format="json")

        self.assertEqual(resposta.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Autor.objects.count(), 1)

    def test_excluir_autor_remove_seus_livros(self):
        autor = Autor.objects.create(nome="Graciliano Ramos")
        Livro.objects.create(titulo="Vidas Secas", ano_publicacao=1938, autor=autor)

        resposta = self.client.delete(reverse("autores-detail", args=[autor.id]))

        self.assertEqual(resposta.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Livro.objects.count(), 0)