from models.mensagens import MSG_CELULAR_INVALIDO, MSG_CELULAR_VAZIO
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Pessoa:
    __LISTA_PREPOSICOES = ["da", "de", "do", "das", "dos", "e"]

    def __init__(self, nome_completo, email, celular, cpf, cep, interesse, genero=None,
                 bairro="", cidade="", estado=""):
        self.__nome_completo = self.__camel_case(nome_completo)
        partes = self.__nome_completo.split()
        self.__primeiro_nome = partes[0]
        self.__segundo_nome = partes[1] if len(partes) > 1 else ""
        if self.__segundo_nome.lower() in self.__LISTA_PREPOSICOES and len(partes) > 2:
            self.__segundo_nome = f"{self.__segundo_nome} {partes[2]}"

        self.email = email
        self.genero = genero
        self.celular = celular
        self.cpf = cpf
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.interesse = interesse
        self.observacoes = []

        if not celular:
            self.observacoes.append(MSG_CELULAR_VAZIO)
        elif len(celular) < 10:
            self.observacoes.append(MSG_CELULAR_INVALIDO)
        if not cpf or len(cpf) != 11:
            self.observacoes.append("CPF inválido")

    def __camel_case(self, texto):
        return ' '.join([
            palavra if palavra in self.__LISTA_PREPOSICOES else palavra.capitalize()
            for palavra in texto.lower().split()
        ])

    @property
    def nome_completo(self): return self.__nome_completo
    @property
    def primeiro_nome(self): return self.__primeiro_nome
    @property
    def segundo_nome(self): return self.__segundo_nome

    def to_dict(self):
        return {
            "nome_completo": self.nome_completo,
            "primeiro_nome": self.primeiro_nome,
            "segundo_nome": self.segundo_nome,
            "genero": self.genero,
            "email": self.email,
            "celular": self.celular,
            "interesse": self.interesse,
            "cpf": self.cpf,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "estado": self.estado,
            "observacoes": "; ".join(self.observacoes)
            }
