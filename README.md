# 📖 Biblioteca API 📖

## Descrição

API REST para gerenciamento de uma biblioteca, desenvolvida com Django e Django REST Framework. Permite cadastrar, consultar, atualizar e excluir **autores** e **livros**, que se relacionam entre si: um autor pode ter vários livros.

A API valida os dados recebidos, e o ano de publicação de um livro não pode ser maior que o ano atual. Os dados são armazenados em SQLite.

---

## Funcionalidades ⚙️

- Cadastro, consulta, atualização e exclusão de autores.
- Cadastro, consulta, atualização e exclusão de livros.
- Relacionamento entre autores e livros.
- Validação dos dados enviados nas requisições.
- Regra de negócio que impede o cadastro de livros com ano de publicação posterior ao ano atual.
- Documentação interativa dos endpoints por meio do Swagger.

---

## Endpoints da API

A API disponibiliza os seguintes endpoints:

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/api/autores/` | Lista os autores |
| POST | `/api/autores/` | Cadastra um autor |
| GET | `/api/autores/{id}/` | Consulta um autor |
| PUT | `/api/autores/{id}/` | Atualiza um autor |
| PATCH | `/api/autores/{id}/` | Atualiza parcialmente um autor |
| DELETE | `/api/autores/{id}/` | Exclui um autor |
| GET | `/api/livros/` | Lista os livros |
| POST | `/api/livros/` | Cadastra um livro |
| GET | `/api/livros/{id}/` | Consulta um livro |
| PUT | `/api/livros/{id}/` | Atualiza um livro |
| PATCH | `/api/livros/{id}/` | Atualiza parcialmente um livro |
| DELETE | `/api/livros/{id}/` | Exclui um livro |

---

## Testes automatizados 🧪

Os testes foram escritos com o `APITestCase` do Django REST Framework e ficam em `biblioteca/tests.py`. Cada teste utiliza um banco de dados temporário, sem afetar os dados do ambiente de desenvolvimento.

### Como executar

Para executar todos os testes do projeto:

```bash
python manage.py test
```

Para executar apenas os testes do aplicativo `biblioteca`, exibindo os detalhes:

```bash
python manage.py test biblioteca -v 2
```

Resultado esperado para o aplicativo `biblioteca`:

```text
Ran 9 tests ... OK
```

---

## 🛠️ Instalação

### Pré-requisitos

- Python instalado.
- Git instalado.

### Passo a passo

**1. Clonar o repositório**

```bash
git clone https://github.com/srlv/biblioteca-api-django.git
cd biblioteca-api-django
```

**2. Criar o ambiente virtual**

```bash
python -m venv venv
```

**3. Ativar o ambiente virtual**

No Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

**4. Instalar as dependências**

```bash
pip install -r requirements.txt
```

**5. Executar as migrações**

```bash
python manage.py migrate
```

**6. Iniciar o servidor**

```bash
python manage.py runserver
```

O servidor estará disponível em:

`http://127.0.0.1:8000/`

---

## Documentação da API 📑

A documentação interativa está disponível por meio do Swagger:

`http://127.0.0.1:8000/swagger/`

Por meio dela, é possível visualizar os endpoints e realizar requisições para testar as funcionalidades da API.