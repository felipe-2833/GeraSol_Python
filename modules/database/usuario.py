import requests

def criar_cliente(data:dict) -> dict:
    url = "http://localhost:8080/api/usuarios"
    response = requests.post(url,json=data)
    response.raise_for_status()
    return response.json()

def visualizar() -> list[dict]:
    url = "http://localhost:8080/api/usuarios"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def visualizar_user(id:int) -> dict:
    url = f"http://localhost:8080/api/usuarios/{id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def atualiza_user(id:int, data:dict):
    url = f"http://localhost:8080/api/usuarios/{id}"
    response = requests.put(url, json=data)
    response.raise_for_status()
    return response.json()

def apagar_user(id:int):
    url = f"http://localhost:8080/api/usuarios/{id}"
    response = requests.delete(url)
    response.raise_for_status()
    