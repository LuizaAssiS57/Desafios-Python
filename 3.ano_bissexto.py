import os

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print("======== QUAL ANO É BISSEXTO? 🤔 ========")

    try:
        ano = int(input("\nInforme um ano: "))
    except ValueError:
        print("Você precisa digitar um ano!")
        input("Aperte Enter para tentar novamente...")
        continue

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        ano_tipo = "bissexto"
    else:
        ano_tipo = "comum"

    print(f"O ano informado é {ano_tipo}!")

    voltar = input("Gostaria de descobrir se outro ano é bissexto? (s/n) ").strip().lower()

    if voltar == "n":
        break

print("======== OBRIGADA POR ACHAR ANOS BISSEXTOS CONOSCO! ;) =======")
