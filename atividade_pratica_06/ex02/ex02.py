#!/usr/bin/env python3

"""
2 - Usuário Aleatório
    Acessa a API Random User Generator para buscar um usuário fictício aleatório.
    Exibe nome, e-mail e país. Caso haja erro na conexão, mostra mensagem de falha.
"""

import requests

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def buscar_usuario():
    url = "https://randomuser.me/api/"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # Lança exceção se status code não for 200

        dados = resposta.json()
        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        return nome, email, pais

    except (requests.RequestException, KeyError):
        return None, None, None

def main():
    print(f"{YELLOW}=== Gerador de Usuário Aleatório Tabajara 3.000 ==={RESET}")

    nome, email, pais = buscar_usuario()

    if nome and email and pais:
        print(f"Nome: {BLUE}{nome}{RESET}")
        print(f"E-mail: {GREEN}{email}{RESET}")
        print(f"País: {YELLOW}{pais}{RESET}")
    else:
        print(f"{RED}Falha ao acessar a API. Tente novamente mais tarde.{RESET}")

if __name__ == "__main__":
    main()

