#!/usr/bin/env python3

"""
4 - Consulta de Cotações de Moedas
    Consulta cotações de moedas em relação ao Real (BRL) usando a API AwesomeAPI.
    Mostra valor atual, máxima, mínima e data/hora da última atualização.
"""

import requests

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def consultar_moeda(sigla):
    url = f"https://economia.awesomeapi.com.br/json/last/{sigla}-BRL"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        chave = f"{sigla.upper()}BRL"
        if chave not in dados:
            return None

        info = dados[chave]
        return {
            "moeda": sigla.upper(),
            "valor": float(info["bid"]),
            "maxima": float(info["high"]),
            "minima": float(info["low"]),
            "data_hora": info["create_date"]
        }

    except (requests.RequestException, ValueError, KeyError):
        return None

def main():
    print(f"{YELLOW}=== Consulta de Moedas Tabajara 3.000 ==={RESET}")
    sigla = input("> Digite a sigla da moeda (ex: USD, EUR): ").strip().upper()

    resultado = consultar_moeda(sigla)

    if resultado:
        print(f"Moeda: {BLUE}{resultado['moeda']}{RESET}")
        print(f"Valor atual: {GREEN}R$ {resultado['valor']:.2f}{RESET}")
        print(f"Máxima do dia: {YELLOW}R$ {resultado['maxima']:.2f}{RESET}")
        print(f"Mínima do dia: {RED}R$ {resultado['minima']:.2f}{RESET}")
        print(f"Última atualização: {BLUE}{resultado['data_hora']}{RESET}")
    else:
        print(f"{RED}Falha ao consultar a moeda. Verifique se a sigla existe ou tente novamente.{RESET}")

if __name__ == "__main__":
    main()

