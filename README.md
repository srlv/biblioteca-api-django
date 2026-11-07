# 📖 Biblioteca API 📖

## Descrição
API REST para gerenciamento de uma biblioteca, desenvolvida com Django e Django REST Framework. Permite cadastrar, consultar, atualizar e excluir **autores** e **livros**, que se relacionam entre si: um autor pode ter vários livros.

A API valida os dados recebidos, e o ano de publicação de um livro não pode ser maior que o ano atual. Os dados são armazenados em SQLite.

---

## Funcionalidades ⚙️ 


---

## Testes automatizados 🧪
Os testes foram escritos com o `APITestCase` do Django REST Framework e ficam em `biblioteca/tests.py`. Cada teste roda em um banco de dados temporário, sem afetar os dados reais.
 
### Como executar
 
```bash
# Todos os testes do projeto
python manage.py test
 
# Apenas os testes do app biblioteca, com o nome de cada teste
python manage.py test biblioteca -v 2
```
 
Resultado esperado para o app `biblioteca`:
 
```
Ran 9 tests ... OK
```

## 🛠️ Instalação

### Pré-requisitos

💻 Ambiente de Desenvolvimento

- Python 3.10.11
- Django 4.2.3
- Django REST Framework 3.14.0
- SQLite

### Passo a Passo
