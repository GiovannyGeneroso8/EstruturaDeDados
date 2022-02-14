"""
Entrar com um ano e informar se o mesmo e bissexto ou nao
"""

while True:
    try:
        Ano = int(input("Informe uma ano: "))
        break
    except ValueError:
        print("Informe um ano valido!")

if Ano % 4 == 0 and Ano % 100 == 0 and Ano % 400 == 0:
        print("O ano: ", Ano," e bissexto!")
elif Ano % 4 == 0 and Ano % 100 != 0:
    print("O ano: ", Ano," e bissexto!")
else:
        print("O ano: ", Ano," não e bissexto!")
