#!/usr/bin/env python3

"""
4 - Calculadora de Consumo de Combustível
    Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:
    * Distância percorrida: 300 km
    * Combustível gasto: 25 litros
    O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def calculate_fuel_consumption(distance, fuel):
    """
    Calcula o consumo médio de combustível (km/l).
    """
    consumption = distance / fuel
    return consumption

def main():
    print(f"{YELLOW}=== Calculadora de Consumo de Combustível Tabajara 3.000 ==={RESET}")

    distance = float(input("> Distância percorrida (km): ") or 300)
    fuel = float(input("> Combustível gasto (litros): ") or 25)

    print(f"{YELLOW}-> Calculando consumo médio...{RESET}")

    consumption = calculate_fuel_consumption(distance, fuel)

    print(f"Distância percorrida: {BLUE}{distance:.2f} km{RESET}")
    print(f"Combustível gasto: {BLUE}{fuel:.2f} litros{RESET}")

    if consumption >= 12:
        color = GREEN
    elif consumption >= 8:
        color = YELLOW
    else:
        color = RED

    print(f"Consumo médio: {color}{consumption:.2f} km/l{RESET}")

if __name__ == "__main__":
    main()

