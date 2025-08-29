import os

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print("===== VERIFICANDO TRIÂNGULOS =====")
    lado_a = float(input("Informe o lado A do triângulo: "))
    lado_b = float(input("Informe o lado B do triângulo: "))
    lado_c = float(input("Informe o lado C do triângulo: "))

    if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a > 0:
        if lado_a == lado_b and lado_a == lado_c:
            print("Triângulo Equilátero")
        elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
            print("Triângulo Isósceles")
        else: 
             print("Triângulo Escaleno")
    else:
        print("Não foi possivel formar um triângulo!")

    voltar = input("Gostaria de verificar outro triâgulo? (s/n) ").strip().lower()

    if voltar == "n":
        break
print("======== OBRIGADA POR VERIFICAR TRIÂNGULOS CONOSCO :) ========")