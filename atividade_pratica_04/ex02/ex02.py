#!/usr/bin/env python3

"""
2 - Registro de Notas e Média da Turma
    Crie um programa que registre as notas dos alunos e calcule a média da turma.
"""

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def main():
    print(f"{YELLOW}=== Registro de Notas da Turma Tabajara 3.000 ==={RESET}")

    notas = []
    while True:
        entrada = input("> Digite a nota do aluno (ou 'sair' para finalizar): ").strip()
        if entrada.lower() == "sair":
            break
        try:
            nota = float(entrada)
            if nota < 0 or nota > 10:
                print(f"{RED}Nota inválida! Digite um valor entre 0 e 10.{RESET}")
                continue
            notas.append(nota)
        except ValueError:
            print(f"{RED}Entrada inválida! Digite um número válido.{RESET}")

    if not notas:
        print(f"{RED}Nenhuma nota registrada.{RESET}")
        return

    media = sum(notas) / len(notas)

    print(f"\n{BLUE}Notas registradas:{RESET} {', '.join(f'{n:.2f}' for n in notas)}")
    print(f"Média da turma: {GREEN}{media:.2f}{RESET}")

if __name__ == "__main__":
    main()
