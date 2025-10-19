#!/usr/bin/env python3

"""
2 - Calculadora de Desconto
    Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

    * Nome do produto: "Camiseta"
    * Preço original: R$ 50.00
    * Porcentagem de desconto: 20%
    O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def calculate_discount(original_price, discount_percentage):
    """
    Calcula o valor do desconto e o preço final.
    """
    discount_value = original_price * (discount_percentage / 100)
    final_price = original_price - discount_value
    return discount_value, final_price

def main():
    print(f"{YELLOW}=== Calculadora de Desconto Tabajara 3.000 ==={RESET}")
    
    # Dados do produto
    product_name = input("> Nome do produto: ") or "Camiseta"
    original_price = float(input("> Preço original do produto (R$): ") or 50.00)
    discount_percentage = float(input("> Porcentagem de desconto (%): ") or 20)

    print(f"{YELLOW}-> Calculando desconto...{RESET}")

    discount_value, final_price = calculate_discount(original_price, discount_percentage)

    # Exibindo resultados com cores
    print(f"Produto: {BLUE}{product_name}{RESET}")
    print(f"Preço original: R$ {BLUE}{original_price:.2f}{RESET}")
    print(f"Desconto ({discount_percentage:.0f}%): R$ {GREEN}{discount_value:.2f}{RESET}")
    print(f"Preço final: R$ {GREEN}{final_price:.2f}{RESET}")

if __name__ == "__main__":
    main()

