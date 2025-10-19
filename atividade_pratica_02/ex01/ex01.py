#!/usr/bin/env python3

"""
1 - Conversor de Moeda
    Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

    * Valor em reais: R$ 100.00
    * Taxa do dólar: R$ 5.20
    * Taxa do euro: R$ 6.15
    O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m" 

def convert_currency(brl_value, us_dollar_exchange_rate, euro_exchange_rate):
    dollar_conversion = brl_value / (us_dollar_exchange_rate * 1.0) # the 1.0 is a hacky way to force flot division.
    euro_conversion = brl_value / (euro_exchange_rate * 1.0)

    converted_values = {
        "us_dollar": dollar_conversion,
        "euro": euro_conversion
    }

    return converted_values

def main():
    print(f"{YELLOW}=== Conversor de moedas tabajara 3.000 ==={RESET}");
    brl_value = float(input("> Entre com o valor em reais que você deseja converter: "))
    us_dollar_exchange_rate = float(input("> Entre com a cotação do dólar: "))
    euro_exchange_rate = float(input("> Entre com a cotação do euro: "))

    converted_values = convert_currency(brl_value, us_dollar_exchange_rate, 
                                       euro_exchange_rate)

    print(f"{YELLOW}-> Convertendo...{RESET}")
    print(f"R$ {BLUE}{brl_value:.2f}{RESET} em dólares, na cotação de {BLUE}$ {us_dollar_exchange_rate:.2f}{RESET} é: {GREEN}$ {converted_values["us_dollar"]:.2f}{RESET}")
    print(f"R$ {BLUE}{brl_value:.2f}{RESET} em euros, na cotação de {BLUE}€ {euro_exchange_rate:.2f}{RESET} é: {GREEN}€ {converted_values["euro"]:.2f}{RESET}")


if __name__ == "__main__":
    main()
