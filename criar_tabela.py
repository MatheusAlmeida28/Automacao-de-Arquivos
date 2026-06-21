import pandas as pd

# Dados estruturados para a planilha
dados = {
    'Produto': ['Notebook Dell', 'Monitor 24"', 'Teclado Logitech', 'Mouse Sem Fio', 'Switch Network 8p'],
    'Quantidade': [5, 12, 25, 30, 4],
    'Valor Unitario': [3500.00, 850.00, 150.00, 80.00, 320.00]
}

# Criar o DataFrame do Pandas
df = pd.DataFrame(dados)

# Gerar o arquivo Excel (.xlsx)
df.to_excel('dados_vendas.xlsx', index=False)

print("Sucesso: O arquivo 'dados_vendas.xlsx' foi criado na pasta atual!")