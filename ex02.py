#!/usr/bin/env python3

OKGREEN = '\033[92m'
FAIL = '\033[91m' 
RESET = '\033[0m'

def calculadora_soma(a, b):
    resultado = None

    if type(a) is int and type(b) is int:
        resultado = a + b

    return resultado

def print_soma(a, b):
    soma = calculadora_soma(a,b)

    if (soma is not None):
        resultado = f"{OKGREEN}{soma} [OK]{RESET}"
    else:
        resultado = f"{FAIL}[Error]{RESET}: Ambos os valores devem ser números válidos"

    print(f"{a} + {b} = {resultado}")

def test_soma():
    test_cases = [
        [12, 14],
        [-12, 12],
        [0, 0],
        [1, 0],
        [0, 1],
        [-12, 14],
        [-12, -12],
        [12, -14],
        ["um", "dois"],
        [1, "dois"],
        ["um", 2],
        ['', ''],
        ['    ', '   3'],
    ]

    for test_case in test_cases:
        print_soma(test_case[0], test_case[1])

if __name__ == "__main__":
    test_soma()
