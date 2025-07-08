class InvalidCPFException(Exception):
    def __init__(self, cpf):
        super().__init__(f"CPF inválido: {cpf}")
