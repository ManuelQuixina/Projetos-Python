import time

def seja_benvindo():
    print("="*56)
    print("="*14, "Conversor de Temperaturas", "="*15)
    print("="*56)
    print()

def graus_celcius(celcius):
    celcius = (5/9) * (valor - 32)
    print(f"{valor}º Graus-Faraday é igual a {celcius} Graus-Celcius")
    if celcius < 0:
        print("Está muito Frio")
    if celcius == 0 and celcius < 10:
        print("Está Frio")
    if celcius == 10 and celcius < 20:
        print("Clima Fresco")
    if celcius == 20 and celcius < 25:
        print("Clima Agradavél")
    if celcius == 25 and celcius < 30:
        print("Clima Quente")

def graus_kelvin(kelvin):
    kelvin = valor - 273.15 
    print(f"{valor}º Graus-kelvin é igual a {kelvin} Graus-Celcius")
    if kelvin < 0:
        print("Está muito Frio")
    if kelvin == 0 and kelvin < 10:
        print("Está Frio")
    if kelvin == 10 and kelvin < 20:
        print("Clima Fresco")
    if kelvin == 20 and kelvin < 25:
        print("Clima Agradavél")
    if kelvin == 25 and kelvin < 30:
        print("Clima Quente")


while True:
    seja_benvindo()
    print("""
        [1] para converter de Faraday em Graus Celcius
        [2] - para converter de Graus-Kelvin em Graus-Celcius
        [3] - para sair""")
    opcao = input("Deseja realizar qual conversão? ")
    print()

    if opcao == "1":
        valor = float(input("Digite o valor da temperatura: [Temp em Faraday]: "))
        graus_celcius(valor)
        continue

    if opcao == "2":
        valor = float(input("Digite o valor da temperatura: [Temp em Keivin]: "))
        graus_kelvin(valor)
        continue

    if opcao == "3":
        print("Finalizando o Programa...")
        time.sleep(2)
        print("Programa Finalizado")
        break
    else:
        print("Opção inválida")
    