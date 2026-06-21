import pandas as pd

def gerar_relatorio():
    try:
        # 1. Ler a planilha do Excel
        # O script espera um arquivo chamado 'dados_vendas.xlsx' com as colunas: 'Produto', 'Quantidade', 'Valor Unitario'
        nome_arquivo = "dados_vendas.xlsx"
        df = pd.read_excel(nome_arquivo)
        
        print(f"-> Arquivo '{nome_arquivo}' lido com sucesso!")

        # 2. Processar os dados
        # Criando uma nova coluna com o faturamento total por linha
        df['Faturamento Total'] = df['Quantidade'] * df['Valor Unitario']
        
        # Calculando métricas para o relatório
        faturamento_geral = df['Faturamento Total'].sum()
        total_itens_vendidos = df['Quantidade'].sum()
        produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().idxmax()

        # 3. Criar e escrever o relatório em um arquivo de texto (.txt)
        nome_relatorio = "relatorio_final.txt"
        with open(nome_relatorio, "w", encoding="utf-8") as arquivo:
            arquivo.write("=========================================\n")
            arquivo.write("       RELATÓRIO DE GESTÃO E VENDAS      \n")
            arquivo.write("=========================================\n\n")
            arquivo.write(f"Faturamento Total: R$ {faturamento_geral:,.2f}\n")
            arquivo.write(f"Quantidade Total de Itens: {total_itens_vendidos}\n")
            arquivo.write(f"Produto Líder em Vendas (Qtd): {produto_mais_vendido}\n\n")
            arquivo.write("-----------------------------------------\n")
            arquivo.write("Detalhamento por Linha:\n")
            arquivo.write("-----------------------------------------\n")
            
            # Iterando sobre as linhas para listar no relatório
            for indice, linha in df.iterrows():
                arquivo.write(f"Produto: {linha['Produto']} | Qtd: {linha['Quantidade']} | Total: R$ {linha['Faturamento Total']:,.2f}\n")
                
            arquivo.write("\n=========================================\n")
            arquivo.write("Relatório gerado automaticamente via Python.\n")

        print(f"-> Sucesso! O relatório '{nome_relatorio}' foi gerado.")

    except FileNotFoundError:
        print(f"Erro: O arquivo 'dados_vendas.xlsx' não foi encontrado. Certifique-se de que ele está na mesma pasta do script.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Executar a função
if __name__ == "__main__":
    gerar_relatorio()