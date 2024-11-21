import requests

def criar_endereco(data:dict) -> dict:
    url = "http://localhost:8080/api/enderecos"
    response = requests.post(url,json=data)
    response.raise_for_status()
    return response.json()

def visualizar_enderecos() -> list[dict]:
    url = "http://localhost:8080/api/enderecos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def visualizar_endereco(id:int) -> dict:
    url = f"http://localhost:8080/api/enderecos/{id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def atualiza_endereco(id:int, data:dict):
    url = f"http://localhost:8080/api/enderecos/{id}"
    response = requests.put(url, json=data)
    response.raise_for_status()
    return response.json()

def apagar_endereco(id:int):
    url = f"http://localhost:8080/api/enderecos/{id}"
    response = requests.delete(url)
    response.raise_for_status()
    




