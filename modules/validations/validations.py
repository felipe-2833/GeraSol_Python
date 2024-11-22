import re

def validar_telefone(telefone):
    padrao = r"^\d{9}$|^\d{5}-\d{4}$|^\d{11}$|^\d{9}-\d{2}$"
    return bool(re.match(padrao, telefone))

def validar_email(email):
    padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(padrao, email))