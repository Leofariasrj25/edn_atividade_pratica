#!/usr/bin/env python3

"""
Uma simples calculadora do preço total de uma compra.
"""

OKGREEN = '\033[92m'
RESET = '\033[0m'

def comprovante_compra(nome_produto, preco_unitario, quantidade):
    return f"""
 [Nome do produto]: {OKGREEN}{nome_produto}{RESET}
 [Preço unitário]: {OKGREEN}R$ {preco_unitario}{RESET}
 [Quantidade]: {OKGREEN}{quantidade}{RESET}
 [Total]: {OKGREEN}R$ {quantidade * preco_unitario}{RESET}"""

def test_compra():
    testes_compra = [
        ["Cadeira Infantil", 12.40, 3],
        ["Mesa", 150.75, 2],
        ["Livro", 45.00, 0],
        ["Brinquedo", 20.0, 5],
        ["Notebook", 3500.50, 1],
        ["Lápis", 0.50, 10],
        ["Copo", 3.75, 2],
        ["Camiseta", 49.90, 5]
    ]

    for test_compra in testes_compra:
        print(comprovante_compra(test_compra[0], test_compra[1], test_compra[2]))

if __name__ == "__main__":
    test_compra()
