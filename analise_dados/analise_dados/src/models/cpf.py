import sys
import os
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)),'../..'))
from exceptions.InvalidCPFException import InvalidCPFException 


class CPF():
    @staticmethod
    def validar_cpf(cpf):
        cpf_tratado = cpf.replace(".", "").replace("-", "")

        if len(cpf_tratado) != 11:
            raise InvalidCPFException(cpf)

        if cpf_tratado == cpf_tratado[0] * 11:
            return False

        primeiro_digito = sum(int(cpf_tratado[i]) * (10 - i) for i in range(9))
        primeiro_digito = (primeiro_digito * 10) % 11
        if primeiro_digito == 10:
            primeiro_digito = 0

        segundo_digito = sum(int(cpf_tratado[i]) * (11 - i) for i in range(9))
        segundo_digito += primeiro_digito * 2
        segundo_digito = (segundo_digito * 10) % 11
        if segundo_digito == 10:
            segundo_digito = 0

        return (
            int(cpf_tratado[-2]) == primeiro_digito and
            int(cpf_tratado[-1]) == segundo_digito
        )
    
if __name__ == "__main__":
    cpfs_para_testar = [
        "529.982.247-25",  # Válido
        "111.111.111-11",  # Inválido
        "123.456.789-00"   # Formato inválido
        ]

    for cpf in cpfs_para_testar:
        try:
            valido = CPF.validar_cpf(cpf)
            print(f"{cpf} -> {'Válido' if valido else 'Inválido'}")
        except InvalidCPFException:
            print(f"{cpf} -> Formato inválido (CPF mal formatado)")