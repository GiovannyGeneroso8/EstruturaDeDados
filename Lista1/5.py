"""
Entrar com a distancia percorrida(KM) e a quantidade de combustivel(L) gasto. Depois informe
quantos quilometros sao percorridos por litro. Sabendo que um carro economico pecorre 15km/l,
diga se o veiculo em questao e economico ou nao.
"""

KM = None
L = None

while True:
    try:
        if KM == None:
            KM = float(input("Informe a quilometragem percorrida: "))
    except ValueError:
        KM = None
        print("Digite apenas numeros!")
    else:
        try: 
            if L == None:
                L = float(input("Informe quantos litros de combustivel foram gastos: "))
                break
        except ValueError:
            L = None
            print("Digite apenas numeros!")

Consumo = KM / L

if Consumo >= 15:
    print("O veiculo e economico com um consumo de: {:.2f} KM/L" .format(Consumo))
else:
    print("O veiculo nao e econimico e tem um consumo de: {:.2f} KM/L" .format(Consumo))

