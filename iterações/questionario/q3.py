maior_salario = 0
contador = 0
while 1:
    nome, salario = input().split(',')
    salario = float(salario)

    maior_salario = max(maior_salario, salario)

    if nome == 'Fim':
        
        break  

    contador += 1

if contador == 0:
    print('Não tem')
else:
    print(maior_salario)

