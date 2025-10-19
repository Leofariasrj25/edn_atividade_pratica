#!/usr/bin/env python3

"""
1 - Gerador de Senhas Aleatórias
    Gera senhas seguras com letras, números e símbolos.
    O usuário escolhe o tamanho da senha.
"""

import random
import string

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print(f"{YELLOW}=== Gerador de Senhas Seguras Tabajara 3.000 ==={RESET}")

    try:
        tamanho = int(input("> Qual o tamanho da senha desejada? "))
        if tamanho <= 0:
            print(f"{RED}Erro: o tamanho deve ser maior que zero.{RESET}")
            return

        senha = gerar_senha(tamanho)
        print(f"Sua senha gerada é: {GREEN}{senha}{RESET}")

    except ValueError:
        print(f"{RED}Erro: digite um número válido para o tamanho.{RESET}")

if __name__ == "__main__":
    main()

