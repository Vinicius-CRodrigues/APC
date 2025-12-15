
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print('Analisando as duas listas originais:')
print(l1)
print(l2)
print('------------------------------------')

l3 = l1 + l2 #Contatenando as duas listas
print('Concatenando a llista 1 com a lista 2:')
print(l3)
print('------------------------------------')
l1.extend(l2) #l1 esta adicionando o valor da l2
print('Extendendo o valor de l1 em l2:')
print(l1)
print('------------------------------------')
l2.append('b') #Insere um novo valor no final da lista.
print('Inserindo um novo valor no final da lista 2:')
print(l2)
print('------------------------------------')
l2.insert(0, 'amor') # Inserir um elemento no indice desejado.
print('Inserindo um elemento no indice desejado(indice zero):')
print(l2)
print('------------------------------------')
l2.pop() #Eliminar o ultimo valor da lista.
print('Eliminando o ultimo valor da lista:')
print(l2)
print('------------------------------------')
del(l3[2:5]) #Excluindo os valores da posição 1 a 4
print('Excluindo os valores da posição 1 a 4 da lista 3:')
print(l3)
print('------------------------------------')



