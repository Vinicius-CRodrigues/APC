contador = 0
menor_salario = 0
menor_nome = ''
primeira_vez = True

while True:
    nome, salario = input().split(',')

    salario = float(salario)

    if nome == 'Fim' or nome == 'fim':
        break
    
    if primeira_vez == True:
        menor_salario = salario
        menor_nome = nome
        primeira_vez = False
    else:
        if salario < menor_salario:
            menor_salario = salario
            menor_nome = nome


    contador += 1





if contador == 0:
    print('Não tem')
else:
    print(menor_nome)

