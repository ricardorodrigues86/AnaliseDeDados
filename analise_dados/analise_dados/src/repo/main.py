import os
from analise_dados.src.repo.gender_service import obter_genero_service
from models.pessoas import Pessoa
from processamento.cliente_processor import ClienteProcessor
from repo.json_repo import salvar_json
from repo.csv_repo import ler_cliente_csv


def escolher_api():
    print("\n Escolha a API de gênero:")
    print("  1 - genderize (gratuita)")
    print("  2 - genderapi (com token)")
    print("  3 - genderapi.io (com token)")
    opcao = input("Digite 1, 2 ou 3: ").strip()
    mapa = {
        "1": "genderize",
        "2": "genderapi",
        "3": "genderapi.io"
    }
    return mapa.get(opcao, "genderize")

def main():
    caminho_csv = "lista_clientes.csv"
    df = ler_cliente_csv(caminho_csv)

    if df.empty:
        print("⚠️ Nenhum dado encontrado no CSV.")
        return

    df.columns = df.columns.str.strip().str.lower()
    print(f"📥 {len(df)} registros carregados de '{caminho_csv}'")

    api = escolher_api()
    genero_service = obter_genero_service(api)

    pessoas = []
    for _, row in df.iterrows():
        nome_raw = str(row.get("nome", "")).strip()
        if not nome_raw:
            print("⚠️ Registro ignorado: nome ausente.")
            continue

        primeiro_nome = nome_raw.split()[0]
        genero = genero_service.inferir(primeiro_nome) or "desconhecido"

        pessoa = Pessoa(
            nome_completo=nome_raw,
            email=row.get("email", ""),
            celular=row.get("celular", ""),
            cpf=row.get("cpf", ""),
            cep=row.get("cep", ""),
            interesse=row.get("interesse", ""),
            genero=genero,
            bairro=row.get("bairro", ""),
            cidade=row.get("cidade", ""),
            estado=row.get("estado", "")
        )
        pessoas.append(pessoa)

    if not pessoas:
        print("⚠️ Nenhum usuário válido foi processado.")
        return

    processor = ClienteProcessor(pessoas)
    processor.exportar_json('saida/usuarios_processados.json')
    processor.gerar_relatorio()

if __name__ == "__main__":
    main()
