#!/usr/bin/env python3

"""
1 - Calculadora de Gorjeta
    Calcula a gorjeta a ser deixada em um restaurante, baseada no valor total da conta
    e na porcentagem de gorjeta desejada.
"""

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

def main():
    print(f"{YELLOW}=== Calculadora de Gorjeta Tabajara 3.000 ==={RESET}")

    try:
        valor_conta = float(input("> Valor total da conta (R$): "))
        porcentagem = float(input("> Porcentagem da gorjeta (%): "))

        gorjeta = calcular_gorjeta(valor_conta, porcentagem)

        print(f"Conta: R$ {BLUE}{valor_conta:.2f}{RESET}")
        print(f"Gorjeta ({porcentagem:.0f}%): R$ {GREEN}{gorjeta:.2f}{RESET}")
        print(f"Total a pagar: R$ {GREEN}{valor_conta + gorjeta:.2f}{RESET}")

    except ValueError:
        print(f"{RED}Erro: entrada inválida! Digite apenas números.{RESET}")

if __name__ == "__main__":
    main()

