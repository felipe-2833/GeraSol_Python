import requests

def visualizar_geradores() -> list[dict]:
    url = "http://localhost:8080/api/geradores"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def visualizar_gerador(id:int) -> dict:
    url = f"http://localhost:8080/api/geradores/{id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def visualizar_pedidos() -> list[dict]:
    url = "http://localhost:8080/api/pedidos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def criar_pedido(data:dict) -> dict:
    url = "http://localhost:8080/api/pedidos"
    response = requests.post(url,json=data)
    response.raise_for_status()
    return response.json()

def criar_aluguel(data:dict) -> dict:
    url = "http://localhost:8080/api/transacoes-aluguel"
    response = requests.post(url,json=data)
    response.raise_for_status()
    return response.json()