import pandas as pd
import os
import json

def salvar_json(pessoas, caminho='saida/usuarios_processados.json'):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    # Converte a lista de objetos em lista de dicionários
    dados = [p.to_dict() for p in pessoas]

    # Cria um DataFrame com os dados
    df = pd.DataFrame(dados)

    # Ordena pelo nome completo
    df = df.sort_values(by='nome_completo', key=lambda col: col.str.lower())

    # Salva como JSON no formato desejado
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump({"users": df.to_dict(orient="records")}, f, ensure_ascii=False, indent=2)