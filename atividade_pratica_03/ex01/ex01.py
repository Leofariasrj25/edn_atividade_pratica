#!/usr/bin/env python3

"""
1 - Classificador de Idade
    Crie um programa que solicite a idade do usuário e classifique-o em uma das seguintes categorias:
    * Criança (0-12 anos)
    * Adolescente (13-17 anos)
    * Adulto (18-59 anos)
    * Idoso (60 anos ou mais)
"""

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def classify_age(age):
    """
    Classifica a idade em uma categoria.
    """
    if 0 <= age <= 12:
        category = "Criança"
        color = BLUE
    elif 13 <= age <= 17:
        category = "Adolescente"
        color = YELLOW
    elif 18 <= age <= 59:
        category = "Adulto"
        color = GREEN
    elif age >= 60:
        category = "Idoso"
        color = RED
    else:
        category = "Idade inválida"
        color = RED
    return category, color

def main():
    print(f"{YELLOW}=== Classificador de Idade Tabajara 3.000 ==={RESET}")

    age = int(input("> Digite sua idade: "))

    category, color = classify_age(age)

    print(f"Você foi classificado como: {color}{category}{RESET}")

if __name__ == "__main__":
    main()

