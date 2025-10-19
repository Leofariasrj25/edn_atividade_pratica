#!/usr/bin/env python3

"""
4 - Calculadora de Dias Vividos
    Calcula quantos dias um indivíduo está vivo de acordo com a data atual.
"""

from datetime import datetime

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def calcular_dias_vividos(data_nascimento):
    hoje = datetime.today()
    delta = hoje - data_nascimento
    return delta.days

def main():
    print(f"{YELLOW}=== Calculadora de Dias Vividos Tabajara 3.000 ==={RESET}")
    print("Digite sua data de nascimento no formato DD/MM/AAAA.")

    try:
        entrada = input("> Data de nascimento: ").strip()
        data_nascimento = datetime.strptime(entrada, "%d/%m/%Y")

        dias_vividos = calcular_dias_vividos(data_nascimento)

        print(f"Você nasceu em: {BLUE}{data_nascimento.strftime('%d/%m/%Y')}{RESET}")
        print(f"Você está vivo há: {GREEN}{dias_vividos} dias{RESET}")

    except ValueError:
        print(f"{RED}Erro: data inválida! Use o formato DD/MM/AAAA.{RESET}")

if __name__ == "__main__":
    main()

