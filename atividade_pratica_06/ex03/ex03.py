#!/usr/bin/env python3

"""
3 - Consulta de CEP
    Consulta informações de um CEP na API ViaCEP e retorna logradouro, bairro, cidade e estado.
    Caso o CEP não exista ou haja erro na requisição, exibe mensagem de falha.
"""

import requests

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # Lança erro se status code não for 200
        dados = resposta.json()

        if "erro" in dados:
            return None

        logradouro = dados.get("logradouro", "")
        bairro = dados.get("bairro", "")
        cidade = dados.get("localidade", "")
        estado = dados.get("uf", "")

        return logradouro, bairro, cidade, estado

    except (requests.RequestException, ValueError):
        return None

def main():
    print(f"{YELLOW}=== Consulta de CEP Tabajara 3.000 ==={RESET}")

    cep = input("> Digite o CEP (somente números): ").strip()

    resultado = consultar_cep(cep)

    if resultado:
        logradouro, bairro, cidade, estado = resultado
        print(f"Logradouro: {BLUE}{logradouro}{RESET}")
        print(f"Bairro: {GREEN}{bairro}{RESET}")
        print(f"Cidade: {YELLOW}{cidade}{RESET}")
        print(f"Estado: {RED}{estado}{RESET}")
    else:
        print(f"{RED}Falha ao consultar o CEP. Verifique se ele existe ou tente novamente mais tarde.{RESET}")

if __name__ == "__main__":
    main()

