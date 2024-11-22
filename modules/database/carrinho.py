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

def atualiza_pedido(id:int, data:dict):
    url = f"http://localhost:8080/api/pedidos/{id}"
    response = requests.put(url, json=data)
    response.raise_for_status()
    return response.json()

def atualiza_aluguel(id:int, data:dict):
    url = f"http://localhost:8080/api/transacoes-aluguel/{id}"
    response = requests.put(url, json=data)
    response.raise_for_status()
    return response.json()

def apagar_pedido(id:int):
    url = f"http://localhost:8080/api/pedidos/{id}"
    response = requests.delete(url)
    response.raise_for_status()
    
def apagar_itens_pedido(id:int):
    url = f"http://localhost:8080/api/itens-pedido/{id}"
    response = requests.delete(url)
    response.raise_for_status()

def apagar_aluguel(id:int):
    url = f"http://localhost:8080/api/transacoes-aluguel/{id}"
    response = requests.delete(url)
    response.raise_for_status()