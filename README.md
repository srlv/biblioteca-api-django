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

---

## Análise de Qualidade e Manutenibilidade do Software

### 1. Objetivo da análise

Com o objetivo de avaliar aspectos relacionados à qualidade e à facilidade de manutenção da Biblioteca API, foi realizada uma análise do código-fonte utilizando ferramentas de análise estática e testes automatizados.

A atividade buscou identificar características estruturais do projeto, verificar a complexidade das implementações existentes, avaliar a cobertura dos testes e apontar possíveis oportunidades de melhoria.

A análise foi conduzida sem alterações nas funcionalidades da aplicação, preservando o comportamento original do sistema.

### 2. Ferramentas utilizadas

Foram utilizadas as seguintes ferramentas:

| Ferramenta         | Finalidade                                                                               |
| ------------------ | ---------------------------------------------------------------------------------------- |
| Radon              | Analisar o tamanho do código, a complexidade ciclomática e o índice de manutenibilidade. |
| Pytest             | Executar os testes automatizados existentes no projeto.                                  |
| pytest-cov         | Identificar a cobertura dos testes e as instruções não executadas.                       |
| ChatGPT            | Apoiar a interpretação dos resultados e a identificação de possíveis melhorias.          |
| Visual Studio Code | Inspecionar os arquivos do projeto e verificar as recomendações apresentadas.            |

A utilização dessas ferramentas permitiu combinar resultados quantitativos com uma avaliação manual de aspectos específicos do código.

### 3. Análise estática do código

A análise estática permite examinar características do código-fonte sem executar diretamente as funcionalidades da aplicação.

Para essa avaliação, foi utilizada a ferramenta Radon, considerando os diretórios `biblioteca`, `users` e `config`.

#### 3.1. Métricas de tamanho

O levantamento das métricas de tamanho foi realizado por meio do comando:

```bash
python -m radon raw biblioteca users config -s
```

Os resultados obtidos foram:

| Métrica                       | Resultado |
| ----------------------------- | --------: |
| Linhas totais (LOC)           |       528 |
| Linhas de código-fonte (SLOC) |       350 |
| Linhas lógicas (LLOC)         |       214 |
| Linhas em branco              |       132 |
| Comentários                   |        24 |

Essas métricas fornecem uma visão quantitativa da estrutura do projeto. Entretanto, a quantidade de linhas, isoladamente, não determina a qualidade do software.

Para uma avaliação mais consistente, é necessário considerar também a complexidade das implementações, a organização dos módulos e a facilidade de compreensão do código.

#### 3.2. Complexidade ciclomática

A complexidade ciclomática foi avaliada com o seguinte comando:

```bash
python -m radon cc biblioteca users config -s -a
```

Foram identificados 31 blocos de código analisados, com complexidade ciclomática média de **1,29**, correspondente à classificação **A** na ferramenta Radon.

Esse resultado indica que os blocos avaliados apresentam, em média, baixa complexidade de fluxo de controle.

A baixa complexidade tende a facilitar a compreensão das implementações e pode contribuir para a elaboração de testes e a realização de futuras modificações.

Entretanto, esse indicador não garante, isoladamente, a ausência de defeitos ou problemas de manutenção.

#### 3.3. Índice de manutenibilidade

O índice de manutenibilidade foi obtido por meio do comando:

```bash
python -m radon mi biblioteca users config -s
```

Entre os resultados registrados, destacam-se:

| Arquivo                         | Classificação | Índice |
| ------------------------------- | ------------- | -----: |
| `biblioteca/models.py`          | A             | 100,00 |
| `biblioteca/tests.py`           | A             |  61,18 |
| `biblioteca/api/serializers.py` | A             |  68,59 |
| `config/settings.py`            | A             |  91,70 |
| `config/urls.py`                | A             |  71,58 |

Os arquivos analisados receberam classificação A, conforme os resultados registrados.

O índice de manutenibilidade combina características do código para estimar sua facilidade de manutenção. Embora os resultados sejam favoráveis, a classificação deve ser interpretada em conjunto com outros indicadores e com a inspeção manual do projeto.

Os comandos, resultados e comentários adicionais estão disponíveis no documento [metricas.md](metricas.md).

### 4. Avaliação dos testes automatizados

Os testes automatizados são importantes para identificar possíveis regressões e oferecer maior segurança durante modificações no software.

Para verificar o funcionamento dos testes existentes, foi utilizado o comando:

```bash
python -m pytest -q
```

A execução apresentou os seguintes resultados:

| Indicador         | Resultado |
| ----------------- | --------: |
| Testes aprovados  |        10 |
| Testes reprovados |         0 |
| Avisos            |         1 |

Todos os dez testes executados foram aprovados.

O aviso apresentado durante a execução não impediu a conclusão dos testes. Entretanto, sua existência deve ser considerada em futuras verificações do ambiente e das dependências do projeto.

### 5. Análise de cobertura dos testes

A cobertura foi avaliada utilizando o `pytest-cov`, com o seguinte comando:

```bash
python -m pytest --cov=biblioteca --cov=users --cov=config --cov-report=term-missing -q
```

O relatório apresentou:

| Indicador                 | Resultado |
| ------------------------- | --------: |
| Instruções analisadas     |       199 |
| Instruções não executadas |        12 |
| Cobertura total           |       94% |

A cobertura total de **94%** indica que uma parcela significativa das instruções consideradas pelo relatório foi executada durante os testes.

É importante destacar que cobertura elevada não significa necessariamente que todas as regras de negócio estejam corretamente verificadas.

A qualidade dos testes também depende da variedade dos cenários avaliados, das verificações realizadas e da capacidade de identificar comportamentos incorretos.

#### 5.1. Arquivos com cobertura inferior

Alguns arquivos apresentaram resultados inferiores à cobertura geral:

| Arquivo                | Cobertura |
| ---------------------- | --------: |
| `biblioteca/models.py` |       87% |
| `biblioteca/views.py`  |        0% |
| `users/views.py`       |        0% |
| `config/asgi.py`       |        0% |
| `config/wsgi.py`       |        0% |

Esses resultados motivaram uma investigação complementar para compreender a função dos arquivos e verificar a necessidade de ampliar os testes.

A análise demonstrou a importância de interpretar os percentuais de cobertura considerando o conteúdo efetivamente implementado em cada módulo.

### 6. Utilização de inteligência artificial como apoio à análise

Como atividade complementar, foi utilizado o ChatGPT para auxiliar na interpretação dos resultados obtidos e na identificação de oportunidades de melhoria relacionadas aos testes automatizados.

A consulta considerou o contexto da Biblioteca API, os dez testes aprovados, a cobertura total de 94% e a existência de arquivos com cobertura de 0%.

A ferramenta recomendou verificar se os arquivos sem cobertura possuíam funcionalidades efetivamente utilizadas pela aplicação antes de propor novos testes.

Também destacou a importância de manter testes para operações de cadastro, consulta, atualização, exclusão e validação de dados, incluindo cenários com entradas inválidas.

#### 6.1. Validação das recomendações

As recomendações foram submetidas a uma verificação manual no Visual Studio Code.

Durante essa inspeção, constatou-se que os arquivos `biblioteca/views.py` e `users/views.py` continham apenas uma importação e o comentário padrão gerado pelo Django, sem funções ou classes de visualização implementadas.

Dessa forma, concluiu-se que a cobertura de 0% desses dois arquivos não representava, por si só, uma deficiência nos testes das funcionalidades reais da API.

Não foram implementados novos testes nesses arquivos, pois não havia funcionalidades próprias a serem verificadas.

Essa atividade demonstrou que recomendações produzidas por inteligência artificial precisam ser avaliadas criticamente antes de serem aplicadas ao projeto.

O registro da consulta, das recomendações e da validação está disponível em [analise_ia.md](analise_ia.md).

### 7. Recomendações para manutenção futura

Com base nos resultados obtidos, foram identificadas algumas ações que podem contribuir para a manutenção contínua da aplicação:

1. **Preservar a execução dos testes automatizados:** executar os testes após alterações no código para identificar possíveis regressões.

2. **Ampliar os cenários de teste quando necessário:** considerar operações de cadastro, consulta, atualização, exclusão e validações de dados, especialmente em situações de erro.

3. **Acompanhar a complexidade do código:** repetir periodicamente a análise com Radon para identificar possíveis aumentos de complexidade decorrentes de novas funcionalidades.

4. **Monitorar a cobertura dos testes:** avaliar as instruções não executadas e verificar se correspondem a comportamentos relevantes para o funcionamento da aplicação.

5. **Manter a documentação atualizada:** registrar alterações importantes, novos procedimentos de execução e mudanças que possam afetar a manutenção do projeto.

6. **Validar recomendações automatizadas:** utilizar ferramentas de inteligência artificial como apoio técnico, sem substituir a inspeção do código e a execução dos testes.

Essas recomendações são preventivas e não representam, necessariamente, problemas identificados no funcionamento atual da aplicação.

### 8. Resultado da análise

Os resultados obtidos indicam características favoráveis à manutenção da Biblioteca API nos aspectos avaliados.

A complexidade ciclomática média de 1,29, a classificação A dos arquivos analisados pelo Radon, a aprovação dos dez testes automatizados e a cobertura total de 94% constituem indicadores positivos.

A inspeção manual também permitiu contextualizar resultados de cobertura aparentemente desfavoráveis, demonstrando que a interpretação das métricas deve considerar a função e o conteúdo dos arquivos.

A utilização de inteligência artificial contribuiu para orientar essa investigação, enquanto a validação manual permitiu verificar a pertinência das recomendações.

A atividade reforça a importância de combinar análise estática, testes automatizados, documentação técnica e revisão humana como práticas de apoio à manutenção e à evolução do software.

### 9. Documentação complementar

Os registros detalhados desta atividade estão disponíveis nos seguintes documentos:

- [Relatório de métricas e cobertura de testes](metricas.md): apresenta os comandos executados, os resultados obtidos e a interpretação dos indicadores de qualidade.
- [Relatório de análise com inteligência artificial](analise_ia.md): apresenta a ferramenta utilizada, o prompt, as recomendações recebidas e a validação manual realizada.


