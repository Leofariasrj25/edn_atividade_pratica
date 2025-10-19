#!/usr/bin/env python3

"""
234 - Verificador de Ano Bissexto
    Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
    Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100)
    que não são divisíveis por 400.
"""

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    print(f"{YELLOW}=== Verificador de Ano Bissexto Tabajara 3.000 ==={RESET}")

    year = int(input("> Digite o ano: "))

    if is_leap_year(year):
        print(f"O ano {BLUE}{year}{RESET} é {GREEN}bissexto{RESET}!")
    else:
        print(f"O ano {BLUE}{year}{RESET} {RED}não é bissexto{RESET}.")

if __name__ == "__main__":
    main()

