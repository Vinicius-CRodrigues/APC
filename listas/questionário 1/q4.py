n = input()


if n == '0':
    print('0.00')
else:
    lista = n.split()

    converter = []

    for i in lista:
        converter.append(int(i))

    soma = converter[0] * 2 + converter[1] * 0.5

    for j in range(2, len(converter)):
        soma = soma * 2 + converter[j] * 0.5
        

    print(f'{soma:.2f}')
     


