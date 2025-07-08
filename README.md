# AnaliseDeDados

Este projeto é uma aplicação Python para manipulação, validação e análise de dados pessoais extraídos de arquivos CSV contendo informações como nome completo, CPF, telefone, CEP, e-mail e áreas de interesse.

A aplicação realiza as seguintes funções principais:

- Validação de CPF: Verifica a validade dos números de CPF informados.
- Consulta e preenchimento de endereço pelo CEP: Obtém dados de endereço (bairro, cidade, estado, DDD) consultando a API ViaCEP.
- Formatação e validação de números de telefone celular.
- Identificação de gênero por meio de APIs externas (Genderize, GenderAPI, Gender API), com escolha da fonte pelo usuário.
- Exportação dos dados processados em formatos CSV e JSON.
- Geração de relatório analítico com informações sobre:
     - Distribuição de gênero
     - Distribuição geográfica por estado
     - Qualidade dos dados (CPFs inválidos, telefones ausentes)
     - Percentual geral por área de interesse
     - Áreas de interesse segmentadas por gênero
