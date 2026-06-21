# Automação de Relatórios com Python e Pandas

Este é um script em Python desenvolvido para automatizar tarefas administrativas repetitivas de extração de dados e geração de relatórios gerenciais a partir de planilhas eletrônicas (Excel).

## 🚀 Funcionalidades

- Leitura automatizada de arquivos `.xlsx` (Excel).
- Processamento de dados e cálculo de métricas (Faturamento Total, Volume de Itens e Produto mais vendido).
- Exportação dos dados processados para um relatório formatado em arquivo de texto (`.txt`).
- Tratamento de exceções para evitar erros de execução caso o arquivo não seja encontrado.

## 🛠️ Tecnologias Utilizadas

- **Python** (Versão 3.x)
- **Pandas**: Para a manipulação e análise estruturada dos dados.
- **Openpyxl**: Engine para suporte de leitura de arquivos modernos do Excel.

## 📦 Como Executar o Projeto

1. Clone o repositório ou baixe o script.
2. Certifique-se de criar um arquivo chamado `dados_vendas.xlsx` com criar_tabela.py na mesma pasta do script com as colunas: `Produto`, `Quantidade` e `Valor Unitario`.
3. Instale as dependências executando:
   ```bash
   pip install pandas openpyxl
