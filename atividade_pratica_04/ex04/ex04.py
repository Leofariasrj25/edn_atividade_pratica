#!/usr/bin/env python3

"""
4 - Classificador de Números
    Analisa números digitados pelo usuário, classificando-os como pares ou ímpares
    e contabilizando quantos de cada tipo foram inseridos.
"""

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def main():
    print(f"{YELLOW}=== Classificador de Números Tabajara 3.000 ==={RESET}")

    count_even = 0
    count_odd = 0

    while True:
        entrada = input("> Digite um número (ou 'sair' para finalizar): ").strip()
        if entrada.lower() == "sair":
            break
        try:
            num = int(entrada)
            if num % 2 == 0:
                print(f"{GREEN}{num} é par.{RESET}")
                count_even += 1
            else:
                print(f"{BLUE}{num} é ímpar.{RESET}")
                count_odd += 1
        except ValueError:
            print(f"{RED}Entrada inválida! Digite um número inteiro.{RESET}")

    print(f"\n{YELLOW}=== Resumo ==={RESET}")
    print(f"Números pares: {GREEN}{count_even}{RESET}")
    print(f"Números ímpares: {BLUE}{count_odd}{RESET}")

if __name__ == "__main__":
    main()
