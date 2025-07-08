import json
from collections import Counter
import os

class ClienteProcessor:
    def __init__(self, clientes):
        self.clientes = sorted(clientes, key=lambda p: p.nome_completo.lower())

    def exportar_json(self, caminho='saida/usuarios_processados.json'):
        usuarios = [p.to_dict() for p in self.clientes]

        # Cria a pasta se não existir
        os.makedirs(os.path.dirname(caminho), exist_ok=True)

        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump({"users": usuarios}, f, ensure_ascii=False, indent=2)

        print(f"✅ JSON exportado para '{caminho}' com {len(usuarios)} usuários.")

    def gerar_relatorio(self):
        total = len(self.clientes)
        generos = Counter(c.genero or "desconhecido" for c in self.clientes)
        interesses = Counter(c.interesse for c in self.clientes if c.interesse)
        telefones_ausentes = sum(1 for c in self.clientes if not c.celular)
        cpfs_invalidos = sum(1 for c in self.clientes if "CPF inválido" in c.observacoes)

        regioes = {
            'Norte': {'AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'},
            'Nordeste': {'AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'},
            'Centro-Oeste': {'DF', 'GO', 'MS', 'MT'},
            'Sudeste': {'ES', 'MG', 'RJ', 'SP'},
            'Sul': {'PR', 'RS', 'SC'}
        }

        distribuicao_regioes = Counter()
        for c in self.clientes:
            uf = c.estado.upper()
            for regiao, estados in regioes.items():
                if uf in estados:
                    distribuicao_regioes[regiao] += 1
                    break

        print(f"\n📊 Relatório de Dados Processados ({total} registros):")
        print(f"• Gênero:")
        for g, q in generos.items():
            print(f"   - {g.capitalize()}: {q / total:.1%}")

        print("• Regiões:")
        for r, q in distribuicao_regioes.items():
            print(f"   - {r}: {q / total:.1%}")

        print(f"• Qualidade dos Dados:")
        print(f"   - Telefones ausentes: {telefones_ausentes}")
        print(f"   - CPFs inválidos: {cpfs_invalidos}")

        print("• Áreas de Interesse (Top 5):")
        for interesse, q in interesses.most_common(5):
            print(f"   - {interesse}: {q / total:.1%}")

        print("• Preferências de interesse por gênero:")
        por_genero = {'male': Counter(), 'female': Counter()}
        for c in self.clientes:
            if c.genero in por_genero and c.interesse:
                por_genero[c.genero][c.interesse] += 1

        for genero, dist in por_genero.items():
            total_g = sum(dist.values())
            if total_g == 0:
                continue
            print(f"   - {genero.capitalize()}:")
            for area, qtd in dist.most_common(3):
                print(f"     • {area}: {qtd / total_g:.1%}")
