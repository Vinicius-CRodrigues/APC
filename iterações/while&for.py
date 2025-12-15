#Descobrindo o numero secreto.

numero_secreto = 7.

#Pedindo a quantidade de tantativas para o programa
while True:
    tentativas = int(input('Digite a quantidade de tentativas que deseja: '))

    if tentativas <= 0:
        print('Numero invalido(digite o numero de tentativas positivo).\n')
    else:
        break

for chute in range(tentativas):
    chute = int(input(f'tentativa {chute + 1} - Digite um numero de 0 a 10: '))

    if chute < numero_secreto:
        print(f'{chute} é menor que o numero secreto.\n')
    elif chute > numero_secreto:
        print(f'{chute} é maior que o numero secreto.\n')
    else:
        print('VOCÊ ACERTOU !')
        break
