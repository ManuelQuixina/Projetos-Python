# Calculadora simples
def visual():
    print("*"*35)
    print()
    print("=========== Calculadora ===========")
    print()
    print("*"*35)
    print()

visual()

#def Calc_adi_sub(mais, menos): 
while True:
    #num1 = int(input("Digite o 1º número: "))
    #num2 = int(input("Digite 2º número: "))
    
    try:
        num1 = int(input("Digite o 1º número: "))
        num2 = int(input("Digite 2º número: "))
        print(""""
    [+] - Operação mais;
    [-] - operação menos;
    [*] - operação multiplicação; 
    [/] - operação divisão
    [0] - para sair""")
        opcao = input("Qual é a operação?: ")

    except ValueError:
        print("Caractere inválido")
        continue
    if opcao == "+":
        adicao = num1 + num2
        print(adicao)
        continue
    if opcao == "-":
        sub = num1 - num2
        print(sub)
        continue    
    if opcao == "*":
        mult = num1 * num2
        print(mult)
        continue
    if opcao == "/":
        div = num1 / num2
        print(div)
        continue
    if opcao == "0":
        print("Finalizando o programa...")
        break
    else:
        print("Opção inválida")
    