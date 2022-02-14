"""

 A partir do saldo bancário inicial, um cliente teve débitos e créditosao longo do mês.
 Faça um algoritmo para ler o saldo inicial, o total de débitos e o total de créditos, e depois 
 escrever o slado final do cliente atráves da mensagem Saldo positivo em R$** ou 
 Saldo negativo em R$** ou Saldo Zero

 """

SaldoInicial = None
Debito = None
Credito = None
while True:
    try:
        if SaldoInicial == None:
            SaldoInicial = float(input("Informe o seu saldo bancario inicial: "))
    except ValueError:
        SaldoInicial = None
        print("Digite apenas números!")
    else:
        try:
            if Debito == None:
                Debito = float(input("Informe o seu total de debitos: "))
        except ValueError:
            Debito = None
            print("Digite apenas números!")
        else:
            try:
                if Credito == None:
                    Credito = float(input("Informe o seu total de creditos: "))
                    break
            except ValueError:
                Credito = None
                print("Digite apenas números!")

SaldoFinal = SaldoInicial + Credito - Debito

if SaldoFinal > 0:
    print("Seu saldo é positivo em R${:.2f}".format(SaldoFinal))
elif SaldoFinal < 0:
    print("Seu saldo é negativo em R${:.2f}".format(SaldoFinal))
else:
    print("Seu saldo é R$0.00")



