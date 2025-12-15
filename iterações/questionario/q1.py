contador = 0
while 1:
    funcionario = input()
    contador += 1
    if funcionario == 'Fim':
        break

print(contador - 1)