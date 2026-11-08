# Métricas do projeto Biblioteca API

## 1. O que fizemos

Analisamos o projeto **Biblioteca API**, feito em Python e Django, para entender o tamanho do código, se ele é complicado e quanto dele foi verificado pelos testes.

Usamos o **Radon** para analisar o código e o **Pytest** para executar os testes.

## 2. Quantidade de linhas

Comando usado:

```powershell
python -m radon raw biblioteca users config -s
```

| Medida | Resultado |
|---|---:|
| Total de linhas (LOC) | 528 |
| Linhas com código (SLOC) | 350 |
| Linhas lógicas de código (LLOC) | 214 |
| Linhas em branco | 132 |
| Comentários | 24 |

**O que significa?** O projeto tem 528 linhas nos arquivos analisados, mas nem todas são código: também existem espaços em branco e comentários. Essa medida mostra o tamanho do projeto, mas não diz, sozinha, se o código é bom ou ruim.

## 3. Complexidade do código

Comando usado:

```powershell
python -m radon cc biblioteca users config -s -a
```

O Radon analisou **31 partes do código**, como funções, classes e métodos. A média foi de aproximadamente **1,29**, com nota **A**.

**O que significa?** A complexidade mostra quantos caminhos e decisões existem no código. Quanto mais decisões, mais difícil uma função pode ficar. A nota A indica que as partes analisadas têm **baixa complexidade**. Isso é bom para entender e mudar o código.

## 4. Facilidade de manutenção

Comando usado:

```powershell
python -m radon mi biblioteca users config -s
```

Os arquivos analisados receberam nota **A**. Alguns exemplos:

| Arquivo | Nota |
|---|---|
| `biblioteca/models.py` | A (100,00) |
| `biblioteca/tests.py` | A (61,18) |
| `biblioteca/api/serializers.py` | A (68,59) |
| `config/settings.py` | A (91,70) |
| `config/urls.py` | A (71,58) |

**O que significa?** Essa medida tenta mostrar se será fácil cuidar do código no futuro. A nota A é positiva, mas não garante que o projeto esteja livre de problemas.

## 5. Testes e cobertura

Primeiro, executamos:

```powershell
python -m pytest -q
```

**Resultado:** 10 testes aprovados e 1 aviso.

Depois, usamos:

```powershell
python -m pytest --cov=biblioteca --cov=users --cov=config --cov-report=term-missing -q
```

| Medida | Resultado |
|---|---:|
| Testes aprovados | 10 |
| Cobertura total | 94% |
| Instruções medidas | 199 |
| Instruções não executadas pelos testes | 12 |

**O que significa?** A cobertura mostra quanto do código foi executado durante os testes. **94% é um resultado alto**, mas não significa que o sistema esteja 94% correto. Os testes ainda podem deixar passar erros.

Alguns arquivos tiveram cobertura menor:

- `biblioteca/models.py`: **87%**.
- `biblioteca/views.py`: **0%**.
- `users/views.py`: **0%**.
- `config/asgi.py` e `config/wsgi.py`: **0%**.

Vale verificar se essas partes precisam de novos testes. Os arquivos `asgi.py` e `wsgi.py` ajudam a iniciar o sistema em certos ambientes, então precisam ser avaliados de acordo com seu uso.

O aviso dos testes veio da biblioteca `pytz` e não impediu a aprovação dos 10 testes.

## 6. O que podemos melhorar

- Verificar as partes que não foram executadas pelos testes.
- Criar mais testes para funções importantes, quando necessário.
- Continuar escrevendo código simples e fácil de entender.
- Repetir as análises depois de fazer mudanças no projeto.

## 7. Conclusão

Os resultados foram bons: o código apresentou **baixa complexidade**, os arquivos analisados receberam **nota A de manutenção** e a **cobertura dos testes chegou a 94%**. Além disso, os **10 testes passaram**.

Esses números mostram que o projeto está em uma boa situação nas medidas que usamos. Mesmo assim, é importante continuar testando e revisando o código.

---

*Resultados registrados em 08/11/2026. Se o projeto mudar, será preciso executar os comandos novamente para atualizar os números.*
