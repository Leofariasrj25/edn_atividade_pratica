#!/usr/bin/env python3

"""
3 - Calculadora de Média Escolar
    Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:
    * Nota 1: 7.5
    * Nota 2: 8.0
    * Nota 3: 6.5
    O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def calculate_average(grades):
    """
    Calcula a média das notas.
    """
    average = sum(grades) / len(grades)
    return average

def main():
    print(f"{YELLOW}=== Calculadora de Média Escolar Tabajara 3.000 ==={RESET}")

    # Entrada de notas (com valores padrão)
    nota1 = float(input("> Nota 1: ") or 7.5)
    nota2 = float(input("> Nota 2: ") or 8.0)
    nota3 = float(input("> Nota 3: ") or 6.5)

    grades = [nota1, nota2, nota3]

    print(f"{YELLOW}-> Calculando média...{RESET}")

    average = calculate_average(grades)

    # Exibindo resultados com cores
    print(f"{BLUE}Notas do aluno:{RESET}")
    for i, nota in enumerate(grades, start=1):
        print(f"Nota {i}: {BLUE}{nota:.2f}{RESET}")
    
    # Cor da média: verde se >= 7, amarelo se >=5, vermelho se <5
    if average >= 7:
        color = GREEN
    elif average >= 5:
        color = YELLOW
    else:
        color = RED

    print(f"Média final: {color}{average:.2f}{RESET}")

if __name__ == "__main__":
    main()

