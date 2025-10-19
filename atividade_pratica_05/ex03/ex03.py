#!/usr/bin/env python3

"""
3 - Calculadora de Preço com Desconto
    Calcula o preço final de um produto após aplicar um desconto percentual.
        a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
        b - Preço final: Determina o novo preço após o desconto.
        c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
        d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
"""

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def calcular_preco_desconto(preco_original, percentual_desconto):
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    return preco_final, valor_desconto

def main():
    print(f"{YELLOW}=== Calculadora de Preço com Desconto Tabajara 3.000 ==={RESET}")

    try:
        preco = float(input("> Preço original do produto (R$): "))
        desconto = float(input("> Percentual de desconto (%): "))

        preco_final, valor_desconto = calcular_preco_desconto(preco, desconto)

        print(f"Preço original: R$ {BLUE}{preco:.2f}{RESET}")
        print(f"Desconto ({desconto:.0f}%): R$ {GREEN}{valor_desconto:.2f}{RESET}")
        print(f"Preço final: R$ {GREEN}{preco_final:.2f}{RESET}")

    except ValueError:
        print(f"{RED}Erro: entrada inválida! Digite apenas números.{RESET}")

if __name__ == "__main__":
    main()

