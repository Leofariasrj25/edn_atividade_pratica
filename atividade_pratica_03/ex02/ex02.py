#!/usr/bin/env python3

"""
2 - Calculadora de IMC
    Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
    O programa deve solicitar o peso (kg) e a altura (m) do usuário, calcular o IMC e
    fornecer a classificação de acordo com a tabela padrão de IMC:
        < 18.5: "Abaixo do peso"
        < 25: "Peso normal"
        < 30: "Sobrepeso"
        >= 30: "Obeso"
"""

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        classification = "Abaixo do peso"
        color = YELLOW
    elif bmi < 25:
        classification = "Peso normal"
        color = GREEN
    elif bmi < 30:
        classification = "Sobrepeso"
        color = RED
    else:
        classification = "Obeso"
        color = RED
    return classification, color

def main():
    print(f"{YELLOW}=== Calculadora de IMC Tabajara 3.000 ==={RESET}")

    weight = float(input("> Digite seu peso (kg): "))
    height = float(input("> Digite sua altura (m): "))

    bmi = calculate_bmi(weight, height)
    classification, color = classify_bmi(bmi)

    print(f"{BLUE}-> Calculando IMC...{RESET}")
    print(f"Peso: {BLUE}{weight:.2f} kg{RESET}")
    print(f"Altura: {BLUE}{height:.2f} m{RESET}")
    print(f"IMC: {GREEN if bmi < 25 else RED}{bmi:.2f}{RESET}")
    print(f"Classificação: {color}{classification}{RESET}")

if __name__ == "__main__":
    main()

