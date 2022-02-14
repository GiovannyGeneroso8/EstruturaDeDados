"""
Uma maquina virtual recebe um valor e exibe o seu quadrado quando ele e par e o seu cubo
quando ele e impar. Faca um algoritmo para esta maquina.
"""

while True:
    try:
        Valor = int(input("Informe um valor inteiro: "))
        break
    except ValueError:
        print("Informe um numero inteiro")

if Valor % 2 == 0:
    print("O quadrado do numero: ", Valor," e: ", Valor ** 2)
else: 
    print("O cubo do numero: ", Valor," e: ", Valor ** 3)