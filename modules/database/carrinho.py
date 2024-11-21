import requests

def visualizar_pedido() -> list[dict]:
    url = "http://localhost:8080/api/pedidos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def visualizar_itens() -> list[dict]:
    url = "http://localhost:8080/api/itens-pedido"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def visualizar_alugueis() -> list[dict]:
    url = "http://localhost:8080/api/transacoes-aluguel"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()