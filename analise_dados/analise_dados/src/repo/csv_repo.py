import os
import pandas as pd

def ler_cliente_csv(file: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file, delimiter=',', encoding='utf-8')
        df.dropna(axis=1, how='all', inplace=True)
        return df
    except FileNotFoundError:
        print(f"Arquivo '{file}' não encontrado.")
    except pd.errors.ParserError:
        print("Erro ao processar o CSV.")
    return pd.DataFrame()


#Visualização dos dados
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_csv = os.path.join(base_dir, "lista_clientes.csv")

    print(f"Lendo: {caminho_csv}")
    csv = ler_cliente_csv(caminho_csv)
    print(csv.head(50))