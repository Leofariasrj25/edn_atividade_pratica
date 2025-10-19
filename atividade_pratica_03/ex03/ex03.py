#!/usr/bin/env python3

"""
3 - Conversor de Temperatura
    Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
    O usuário deve informar a temperatura, a unidade de origem e a unidade de destino.
"""

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def convert_temperature(value, from_unit, to_unit):
    """
    Converte a temperatura entre Celsius, Fahrenheit e Kelvin.
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    # Primeiro converte para Celsius
    if from_unit == "c":
        celsius = value
    elif from_unit == "f":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "k":
        celsius = value - 273.15
    else:
        raise ValueError("Unidade de origem inválida! Use C, F ou K.")

    # Depois converte de Celsius para a unidade desejada
    if to_unit == "c":
        return celsius
    elif to_unit == "f":
        return celsius * 9 / 5 + 32
    elif to_unit == "k":
        return celsius + 273.15
    else:
        raise ValueError("Unidade de destino inválida! Use C, F ou K.")

def main():
    print(f"{YELLOW}=== Conversor de Temperatura Tabajara 3.000 ==={RESET}")

    value = float(input("> Digite a temperatura: "))
    from_unit = input("> Unidade de origem (C/F/K): ")
    to_unit = input("> Unidade de destino (C/F/K): ")

    try:
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{BLUE}-> Convertendo...{RESET}")
        print(f"{value:.2f} {BLUE}{from_unit.upper()}{RESET} equivalem a {GREEN}{result:.2f} {to_unit.upper()}{RESET}")
    except ValueError as e:
        print(f"{RED}Erro: {e}{RESET}")

if __name__ == "__main__":
    main()

