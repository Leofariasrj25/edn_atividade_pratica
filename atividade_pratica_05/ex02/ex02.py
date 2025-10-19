#!/usr/bin/env python3

"""
2 - Verificador de Palíndromo
    Verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente),
    ignorando espaços e pontuação.
"""

import string

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def eh_palindromo(texto):
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    return texto_limpo == texto_limpo[::-1]

def main():
    print(f"{YELLOW}=== Verificador de Palíndromo Tabajara 3.000 ==={RESET}")

    frase = input("> Digite uma palavra ou frase: ")

    if eh_palindromo(frase):
        print(f"{GREEN}Sim!{RESET} É um palíndromo.")
    else:
        print(f"{RED}Não!{RESET} Não é um palíndromo.")

if __name__ == "__main__":
    main()

