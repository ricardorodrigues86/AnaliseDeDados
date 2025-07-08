import os
import requests

class GenderServiceBase:
    def inferir(self, nome): raise NotImplementedError()

class GenderizeService(GenderServiceBase):
    def inferir(self, nome):
        try:
            r = requests.get(f"https://api.genderize.io/?name={nome}")
            return r.json().get("gender") if r.ok else None
        except:
            return None

class GenderAPIService(GenderServiceBase):
    def inferir(self, nome):
        token = os.getenv("GENDERAPI_TOKEN")
        if not token: return None
        try:
            r = requests.get(f"https://gender-api.com/get?key={token}&name={nome}")
            return r.json().get("gender") if r.ok else None
        except:
            return None

class GenderApiIOService(GenderServiceBase):
    def inferir(self, nome):
        token = os.getenv("GENDERAPIO_TOKEN")
        if not token: return None
        try:
            r = requests.get(f"https://genderapi.io/api/?key={token}&name={nome}")
            return r.json().get("gender") if r.ok else None
        except:
            return None

def obter_genero_service(api_nome):
    match api_nome:
        case "genderize": return GenderizeService()
        case "genderapi": return GenderAPIService()
        case "genderapi.io": return GenderApiIOService()
        case _: raise ValueError(f"API de gênero desconhecida: {api_nome}")