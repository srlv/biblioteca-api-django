# 📚 Biblioteca API

API REST para gerenciamento de autores e livros, desenvolvida com Python, Django e Django REST Framework, utilizando SQLite para armazenamento dos dados.

## Sumário

- [Descrição](#1-descrição)
- [Tecnologias](#2-tecnologias)
- [Entidades e relacionamento](#3-entidades-e-relacionamento)
- [Regras de negócio](#4-regras-de-negócio)
- [Funcionalidades](#5-funcionalidades)
- [Endpoints](#6-endpoints)
- [Instalação e execução](#7-instalação-e-execução)
- [Documentação da API](#8-documentação-da-api)
- [Testes automatizados](#9-testes-automatizados)
- [Análise de qualidade e manutenibilidade](#10-análise-de-qualidade-e-manutenibilidade)
- [Utilização de IA](#11-utilização-de-ia)
- [Documentação complementar](#12-documentação-complementar)

---

## 1. Descrição

A Biblioteca API permite cadastrar, consultar, atualizar e excluir autores e livros, mantendo o relacionamento entre essas entidades.

## 2. Tecnologias

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem de programação |
| Django | Framework web |
| Django REST Framework | Desenvolvimento da API REST |
| SQLite | Banco de dados |
| Swagger / OpenAPI | Documentação da API |
| Pytest | Testes automatizados |
| pytest-cov | Cobertura dos testes |
| Radon | Análise de métricas |
 
## 3. Entidades e relacionamento

A aplicação possui duas entidades principais:

- **Autor:** representa os autores cadastrados.
- **Livro:** representa os livros da biblioteca.

**Relacionamento:** um autor pode possuir vários livros, enquanto cada livro está associado a um autor (1:N).

## 4. Regras de negócio

| ID | Regra | Descrição |
|---|---|---|
| RN01 | Relacionamento entre autores e livros | Um autor pode possuir vários livros, e cada livro deve estar associado a um autor. |
| RN02 | Validação do ano de publicação | Não é permitido cadastrar livros com ano de publicação posterior ao ano atual. |
| RN03 | Validação dos dados | Os dados enviados nas requisições devem passar pelas validações dos serializers antes de serem processados. |

## 5. Funcionalidades

- Cadastro, consulta, atualização e exclusão de autores.
- Cadastro, consulta, atualização e exclusão de livros.
- Associação de livros aos seus respectivos autores.
- Validação dos dados enviados nas requisições.
- Verificação do ano de publicação dos livros.

## 6. Endpoints

### Autores

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/api/autores/` | Lista autores |
| POST | `/api/autores/` | Cadastra autor |
| GET | `/api/autores/{id}/` | Consulta autor |
| PUT | `/api/autores/{id}/` | Atualiza autor |
| PATCH | `/api/autores/{id}/` | Atualiza parcialmente autor |
| DELETE | `/api/autores/{id}/` | Exclui autor |

### Livros

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/api/livros/` | Lista livros |
| POST | `/api/livros/` | Cadastra livro |
| GET | `/api/livros/{id}/` | Consulta livro |
| PUT | `/api/livros/{id}/` | Atualiza livro |
| PATCH | `/api/livros/{id}/` | Atualiza parcialmente livro |
| DELETE | `/api/livros/{id}/` | Exclui livro |

---

## 7. Instalação e execução

### Pré-requisitos

- Python instalado.
- Git instalado.

### 1. Clonar o repositório

```bash
git clone https://github.com/srlv/biblioteca-api-django.git
cd biblioteca-api-django
```

### 2. Criar o ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar as migrações

```bash
python manage.py migrate
```

### 6. Iniciar o servidor

```bash
python manage.py runserver
```

A aplicação estará disponível em:

`http://127.0.0.1:8000/`

## 8. Documentação da API

A documentação interativa está disponível pelo Swagger:

`http://127.0.0.1:8000/swagger/`

Nela é possível visualizar os endpoints e realizar requisições para testar as funcionalidades da API.

## 9. Testes automatizados

Os testes foram desenvolvidos utilizando `APITestCase` do Django REST Framework e estão localizados em `biblioteca/tests.py`.

**Executar todos os testes pelo Django:**

```bash
python manage.py test
```

**Executar os testes do aplicativo biblioteca:**

```bash
python manage.py test biblioteca -v 2
```

Resultado registrado:

```text
Ran 9 tests ... OK
```

Também foi realizada uma execução utilizando Pytest:

```bash
python -m pytest -q
```

| Indicador | Resultado |
|---|---:|
| Testes aprovados | 10 |
| Testes reprovados | 0 |
| Avisos | 1 |

## 10. Análise de qualidade e manutenibilidade

Foram utilizadas ferramentas de análise estática e testes automatizados para avaliar a qualidade e a facilidade de manutenção do projeto.

### Métricas coletadas

| Métrica | Resultado |
|---|---:|
| Linhas totais (LOC) | 528 |
| Linhas de código-fonte (SLOC) | 350 |
| Complexidade ciclomática média | 1,29 (A) |
| Cobertura dos testes | 94% |
| Instruções analisadas | 199 |
| Instruções não executadas | 12 |

### Índice de manutenibilidade

| Arquivo | Classificação | Índice |
|---|---|---:|
| `biblioteca/models.py` | A | 100,00 |
| `biblioteca/tests.py` | A | 61,18 |
| `biblioteca/api/serializers.py` | A | 68,59 |
| `config/settings.py` | A | 91,70 |
| `config/urls.py` | A | 71,58 |

Os resultados indicam baixa complexidade ciclomática, classificação A nos arquivos avaliados pelo Radon e cobertura de testes de 94%.

Os dados detalhados e os comandos utilizados estão disponíveis em [metricas.md](metricas.md).

## 11. Utilização de IA

O ChatGPT foi utilizado como apoio à interpretação das métricas e à identificação de possíveis melhorias nos testes automatizados.

As recomendações foram verificadas manualmente no Visual Studio Code. Durante a inspeção, constatou-se que os arquivos `biblioteca/views.py` e `users/views.py` não possuíam funcionalidades próprias implementadas, justificando a cobertura de 0% desses arquivos.

A análise demonstrou a importância de validar as sugestões da inteligência artificial antes de aplicá-las ao projeto.

O prompt utilizado, as recomendações e a validação estão disponíveis em [analise_ia.md](analise_ia.md).

## 12. Documentação complementar

- [metricas.md](metricas.md): comandos executados, resultados das métricas e análise da cobertura dos testes.
- [analise_ia.md](analise_ia.md): prompt utilizado, resposta da IA e validação das recomendações.