"""
Na escola Meu Jardim o aluno recebe quatro notas por 
disciplina. Faça um algoritmo para entrar com quatro notas,
o nome do aluno, calcular a média e dizer se o aluno foi
aprovado ou reprovado. Considere aprovação para valor de
média igual ou superior a seis.
"""

#classe responsavem pela limpeza da tela do cmd
from os import system
system('cls')

#selecao da quantidade de notas utilizadas para calcular a media
while True:
    try:
        print("""Selecione a forma que é calculada a média na instituição: \n
        1- Duas notas \n
        2- Três notas \n
        3- Quatro notas \n\n """)
        opcao = int(input("Qual a modalidade desejada: "))
        if opcao < 1 or opcao > 3:
            raise ValueError
        else:
            if opcao == 1 : quantNotas = 3 
            elif opcao == 2: quantNotas = 4
            else: quantNotas = 5
            break
    except ValueError:
        system('cls')
        print("=-"*32)
        print("Selecione uma opção valida!")
        print("=-"*32)

#Configvetor: a primeira posicao do vetor sera reservada para o nome do aluno e a ultima para a media
dados = []
for i in range(quantNotas): dados.append(None) 

#validacao da entrada das notas do aluno
while True:
    try:
        for i in range(quantNotas):
            if i == 0 and dados[0] == None:
                system('cls')
                print("=-"*32)
                dados[i] = input("Qual o nome do aluno: ")
                print("=-"*32)
            else:
                if dados[i] == None:
                    dados[i] = float(input(f"Informe a {i}° nota do {dados[0]}: "))
                    if dados[i] < 0 or dados[i] > 10 : raise ValueError 
        break
    except ValueError:
        dados[i] = None
        i -= 1
        
#calculo da media da nota do aluno
dados.append(float(0))
for i  in range (1, quantNotas):
    dados[quantNotas] += dados[i]
dados[quantNotas] /= (quantNotas - 1)

#verificacao se o aluno foi reprovado ou aprovado
if dados[quantNotas] < 6:
    print("=-" * 32)
    print(f"O aluno {dados[0]}, teve a média: {dados[quantNotas]:.2f}, portanto está reprovado!")
    print("=-" * 32)
else:
    print("=-" * 32)
    print(f"O aluno {dados[0]}, teve a média: {dados[quantNotas]:.2f}, portanto está aprovado!")
    print("=-" * 32)


