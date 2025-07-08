import csv
import requests
import re

class Cliente:
    def __init__(self, nome, cep: str):
        self.nome = nome.strip()
        self.cep = self.limpar_cep(cep)
        self.bairro = None
        self.cidade = None
        self.estado = None

    def limpar_cep(self, cep_raw):
        return re.sub(r'\D', '', cep_raw)

    def cep_valido(self):
        return len(self.cep) == 8 and self.cep.isdigit()

    def buscar_endereco(self):
        if not self.cep_valido():
            print(f"⚠️ CEP inválido para {self.nome}: {self.cep}")
            return

        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        try:
            response = requests.get(url)
            response.raise_for_status()
            dados = response.json()

            if "erro" in dados:
                print(f"❌ CEP não encontrado: {self.cep}")
                return

            self.bairro = dados.get("bairro")
            self.cidade = dados.get("localidade")
            self.estado = dados.get("uf")
        except requests.RequestException as e:
            print(f"Erro ao buscar o CEP {self.cep} para {self.nome}: {e}")

    def __str__(self):
        return f"{self.nome} - {self.cep} - {self.bairro}, {self.cidade} - {self.estado}"

if __name__ == "__main__":
    cliente = Cliente("Ricardo", "50670-330")
    cliente.buscar_endereco()
    print(cliente)
    