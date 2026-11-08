# Análise de Inteligência Artificial – Biblioteca API

## 1. Ferramenta utilizada

Foi utilizado o ChatGPT como ferramenta de apoio à análise da qualidade dos testes automatizados da API de biblioteca, desenvolvida com Django REST Framework.

## 2. Prompt utilizado

Estou analisando a manutenção de uma API de biblioteca desenvolvida em Django REST Framework. Executei os testes automatizados com Pytest e obtive 10 testes aprovados e cobertura total de 94%. Os arquivos biblioteca/views.py e users/views.py apresentaram 0% de cobertura. Quais melhorias você recomenda para aumentar a qualidade dos testes e facilitar a manutenção do projeto? Explique de forma simples, sem modificar o código.

## 3. Resposta da IA

A IA recomendou verificar se os arquivos com cobertura de 0% possuem funcionalidades utilizadas pela aplicação. Caso possuam, seria importante criar testes específicos. Entretanto, se forem arquivos sem funcionalidades implementadas, não é necessário criar testes apenas para aumentar a porcentagem de cobertura.

A IA também recomendou manter testes para operações de cadastro, consulta, atualização, exclusão e validações de negócio, incluindo situações com dados inválidos.

## 4. Validação da sugestão

Foram inspecionados manualmente os arquivos biblioteca/views.py e users/views.py no VS Code. Ambos contêm apenas a importação de render e um comentário padrão do Django, sem funções ou classes de visualização implementadas.

Por isso, concluiu-se que a cobertura de 0% nesses arquivos não indica, por si só, uma falha nos testes das funcionalidades reais da API. A análise não substitui a verificação dos endpoints implementados em outros arquivos.

## 5. Decisão e conclusão

A sugestão da IA foi utilizada como orientação para uma inspeção manual do código, mas não foi necessário implementar novos testes nesses dois arquivos. Nenhum código foi alterado nesta etapa.

A análise reforçou a importância de interpretar os relatórios de cobertura considerando o conteúdo e a função de cada arquivo, em vez de buscar apenas aumentar o percentual total.