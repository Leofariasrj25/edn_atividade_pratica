#!/usr/bin/env python3

"""
3 - Verificador de Senha
    Verifica se a senha digitada pelo usuário atende a critérios básicos de segurança:
        a) Deve ter pelo menos 8 caracteres.
        b) Deve conter pelo menos um número.
"""

# Cores para o terminal
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def is_valid_password(password):
    has_min_length = len(password) >= 8
    has_number = any(char.isdigit() for char in password)
    return has_min_length, has_number

def main():
    print(f"{YELLOW}=== Verificador de Senha Tabajara 3.000 ==={RESET}")

    password = input("> Digite sua senha: ")

    has_min_length, has_number = is_valid_password(password)

    if has_min_length and has_number:
        print(f"{GREEN}Senha válida! ✅{RESET}")
    else:
        print(f"{RED}Senha inválida! ❌{RESET}")
        if not has_min_length:
            print(f"{RED}- Deve ter pelo menos 8 caracteres.{RESET}")
        if not has_number:
            print(f"{RED}- Deve conter pelo menos um número.{RESET}")

if __name__ == "__main__":
    main()

