import os

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print("======== BEM VINDO AO NOSSO CAIXA ELETRÔNICO ========")
    vlr_saque = int(input("Qual o valor que deseja sacar? Ou digite 0 para sair da operação. "))

    if vlr_saque == 0:
        break

    vlr_original = vlr_saque

    qtd_100 = vlr_saque // 100
    vlr_saque = vlr_saque % 100

    qtd_50 = vlr_saque // 50
    vlr_saque = vlr_saque % 50
    
    qtd_20 = vlr_saque // 20
    vlr_saque = vlr_saque % 20

    qtd_10 = vlr_saque // 10
    vlr_saque = vlr_saque % 10

    qtd_5 = vlr_saque // 5
    vlr_saque = vlr_saque % 5

    qtd_2 = vlr_saque // 2
    vlr_saque = vlr_saque % 2

    print("======== FINALIZANDO CONTAGEM DE NOTAS ========")
    print(f"\nO valor solicitado foi R${vlr_original}, você receberá:")
    print(f"{qtd_100} notas de R$100 ")
    print(f"{qtd_50} notas de R$50 ")
    print(f"{qtd_20} notas de R$20 ")
    print(f"{qtd_10} notas de R$10 ")
    print(f"{qtd_5} notas de R$5 ")
    print(f"{qtd_2} notas de R$2 ")

    input("Precione Enter para voltar a tela inicial.")

print("======== OBRIGADO POR USAR O NOSSO CAIXA ELETRÔNICO :) ========")