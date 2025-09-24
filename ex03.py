#!/usr/bin/env python3

"""
Uma simples calculadora de volume.
"""

OKGREEN = '\033[92m'
FAIL = '\033[91m'
RESET = '\033[0m'

def is_numeric(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)

def calculadora_volume(a, b, c):
    result = None
    if is_numeric(a) and is_numeric(b) and is_numeric(c):
        result = a * b * c
    return result

def print_volume(a, b, c):
    volume = calculadora_volume(a, b, c)
    if volume is not None:
        resultado = f"{OKGREEN}{volume}cm³ [OK]{RESET}"
    else:
        resultado = f"{FAIL}[Error]{RESET}: Todos os valores devem ser números válidos"
    print(f"{a} + {b} + {c} = {resultado}")

def test_volume():
    test_cases = [
        [0, 0, 0],
        [1, 2, 3],
        [-1, -2, -3],
        [3.14, 2.71, 1.41],
        [100, 0, -50],
        [-7.5, 4.2, 0],
        [999999, -999999, 123456],
        [0.0001, -0.0001, 0.0],
        [0, 0, "0"],
        [0, "zero", 0],
        ["000", 0, 0],
        ["um", "dois", "tres"],
    ]

    for test_case in test_cases:
        print_volume(test_case[0], test_case[1], test_case[2])

if __name__ == "__main__":
    test_volume()
