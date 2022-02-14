"""
O indice de massa corporea (IMC) e calculado a partir da seguinte formula:
IMC = peso(KG)/altura(M)
Faca um algoritmo para calcular e imprimir o IMC de uma pessoa, e depois exibir
uma das seguintes mensagens:

IMC     Clasificacao
<18.5   Abaixo do peso
<25     Peso normal
<30     Sobre peso
<40     Obeso moderado
>=40    Obeso morbio
"""

Peso = None
Altura = None
while True:
    try:
        if Peso == None:
            Peso = float(input("Informe seu peso em KG: "))
    except ValueError:
        Peso = None
        print("Digite apenas numeros!")
    else:
        try:
            if Altura == None:
                Altura = float(input("Informe sua altura em M: "))
                break
        except ValueError:
            Altura = None
            print("Digite apenas numeros!")

IMC = Peso / (Altura**2)

if IMC < 18.5:
    print("Seu IMC e: {:.2f} e voce esta abaixo do peso".format(IMC))
elif IMC < 25:
    print("Seu IMC e: {:.2f} e voce esta no peso normal".format(IMC))
elif IMC < 30:
    print("Seu IMC e: {:.2f} e voce esta com sobrepeso".format(IMC))
elif IMC < 35:
    print("Seu IMC e: {:.2f} e voce e um obeso leve".format(IMC))
elif IMC < 40:
    print("Seu IMC e: {:.2f} e voce e um obeso moderado".format(IMC))
else: 
    print("Seu IMC e: {:.2f} e voce e um obeso morbido".format(IMC))