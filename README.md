# FinanceHub

Aplicação em Python voltada para simulação de investimentos e planejamento financeiro.

O projeto foi desenvolvido em grupo durante a graduação, com o objetivo de aplicar conceitos de programação modular, manipulação de dados, integração com APIs e testes automatizados.

## Funcionalidades

- Cadastro e autenticação de usuários
- Atualização de dados do usuário
- Simulação de aposentadoria
- Simulação de investimentos
- Consulta de indicadores financeiros
- Histórico das simulações realizadas
- Cálculo de juros compostos
- Cálculo de renda passiva
- Ajuste de valores pela inflação
- Testes automatizados

## Integração com API

O projeto utiliza dados do Banco Central do Brasil para consultar indicadores financeiros através da API SGS.

Entre os indicadores utilizados estão:

- Selic
- CDI
- IPCA
- Poupança

Caso a API esteja indisponível, o sistema possui valores padrão para permitir a execução da aplicação.

## Tecnologias

- Python
- API SGS - Banco Central do Brasil
- JSON
- Pytest
- Git e GitHub

## Estrutura do projeto

```text
FinanceHub/
├── entidades/
│   ├── CalculoFinanceiro.py
│   └── gerenciadorDeUsuario.py
│
├── interface/
│   └── telas.py
│
├── servicos/
│   ├── consultor_bcb.py
│   └── simuladores.py
│
├── testes/
│   ├── test_calculo_financeiro.py
│   ├── test_consultor_bcb.py
│   ├── test_gerenciador_usuario.py
│   └── test_simuladores.py
│
├── main.py
├── usuarios_exemplo.json
└── .gitignore