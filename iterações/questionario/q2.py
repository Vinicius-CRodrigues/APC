contador = 0
total_salario = 0
media = 0

while 1:
    nome, salario = input().split(',')

    if nome == 'Fim':
        print(f'{media:.2f}')
        break
    else:
        salario = float(salario)
        total_salario = total_salario + salario
        contador += 1
        media = total_salario / contador