#!/usr/bin/env python3

"""
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
"""

import operator

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

# Dicionário de estratégias
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def main():
    print(f"{YELLOW}=== Calculadora Básica (Strategy) Tabajara 3.000 ==={RESET}")

    try:
        num1 = float(input("> Digite o primeiro número: "))
        num2 = float(input("> Digite o segundo número: "))
        print("> Operações disponíveis: +, -, *, /")
        operation = input("> Escolha a operação: ").strip()

        if operation not in operations:
            print(f"{RED}Operação inválida! Use +, -, * ou /{RESET}")
            return

        if operation == "/" and num2 == 0:
            print(f"{RED}Erro: divisão por zero não é permitida!{RESET}")
            return

        # Strategy pattern: seleciona a função correspondente
        func = operations[operation]
        result = func(num1, num2)

        print(f"{BLUE}{num1} {operation} {num2}{RESET} = {GREEN}{result:.2f}{RESET}")

    except ValueError:
        print(f"{RED}Erro: entrada inválida! Digite apenas números.{RESET}")

if __name__ == "__main__":
    main()

