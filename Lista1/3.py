"""
Os ingressos do cinema custam X reais. Na terca-feira ha um descontro de 50%, e em qualquer
dia, menores de 14 anos tambem tem um desconto de 50%. Faca um algoritmo que, sendo lidos o
dia da semna, a idade do espectador e o preco base do ingresso, imprima o valor a pagar. 
Considere que 1 e domingo, 2 e segunda, etc. Ex.: ingresso na terca para um espectador de 
11 anos, com preco-base de R$12.00 - o valor a pagar e de R$3.00.
"""

Dia = None
Idade = None
ValorBase = None

while True:
    try:
        if Dia == None:
            Dia = int(input("Informe o dia da semana: "))
            
            if Dia < 1 or Dia > 7:
                Error()
    except ValueError:
        Dia = None
        print("Digite somente numeros inteiros entre 1 e 7!")
    except:
        Dia = None
        print("Digite somente numeros entre 1 e 7!")
    else:
        try:
            if Idade == None:
                Idade = int(input("Informe a sua idade: "))
                try:
                    if Idade < 1 or Idade > 150:
                        Error()
                except:
                    Idade = None
                    print("Informe uma idade valida!")
        except ValueError:
            Idade = None
            print("Informe uma idade valida!")
        else:
            try:
                if ValorBase == None:
                    ValorBase = float(input("Informe o valor base do ingresso: R$"))
                    break
            except ValueError:
                ValorBase = None
                print("Digite apenas numeros!")

ValorFinal = ValorBase

if Idade < 14:
    ValorFinal = ValorFinal - ValorFinal * 0.5
if Dia == 3:
    ValorFinal = ValorFinal - ValorFinal * 0.5

print("O valor base do ingresso e de: R${:.2f} e com os descontos voce pagara R${:.2f}"
.format(ValorBase, ValorFinal))
