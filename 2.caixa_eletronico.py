import os
from colorama import init, Fore, Style

init(autoreset=True)

NOTAS = [100, 50, 20, 10, 5, 2]

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print("======== BEM VINDO AO NOSSO CAIXA ELETRÔNICO ========")

    try:
        vlr_saque = int(input("Qual o valor que deseja sacar? Ou digite 0 para sair da operação. "))

        if vlr_saque == 0:
            break

        if vlr_saque < 0:
            print("Valor inválido")
            input("Aperte Enter para continuar.")
            continue

        vlr_original = vlr_saque
        resultado = {}

        for nota in NOTAS:
            if vlr_saque >= nota:
                qtd = vlr_saque // nota
                resultado[nota] = qtd
                vlr_saque %= nota

        print("======== FINALIZANDO CONTAGEM DE NOTAS ========")
        print(f"\nO valor solicitado foi R${vlr_original}, você receberá:")

        for nota, quantidade in resultado.items():
            print(f"{quantidade} nota(s) de R${nota}")

        if vlr_saque > 0:
            print(f"Restante: {vlr_saque} (Não será possivel sacar com as notas disponiveis.)")

    except ValueError:
        print("Por favor digite um valor numerico válido!")

    input("Precione Enter para voltar a tela inicial.")

print("======== OBRIGADO POR USAR O NOSSO CAIXA ELETRÔNICO :) ========")