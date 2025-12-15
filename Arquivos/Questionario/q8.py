import os

file = input()

lista = []

if os.path.isfile(file[22:]) == True:
    with open(file[22:], 'r') as arquivo:

        print('da pra abrir')
        linhas = arquivo.readlines()
        for linha in linhas:
            nome, numero = linha.strip().split()
            numero = int(numero)
            lista.append((nome, numero))
        lista.sort(key= lambda x: x[1], reverse=True)

        for itens in lista:
            print(itens)
            


else:
    print('nao da pra abrir')
