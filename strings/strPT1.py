# STRINGS - Cadeias de caracteres

frase = 'Olá pessoal, tudo certo por ai ?'

#Para pegar elementos dentro da frase eu uso:
print(frase[0])

#Para pegar frações (fatiamento) da string eu uso(intervalo fechado no inicio e aberto no final):
print(frase[0:8]) # Ele irá pegar de 0 até 7.

print(frase[6:10])

#Posso configurar o passo de caminhada pela string.
print(frase[0:11:2])

#Posso pegar a string pelo tamanho dela ou ela inteira com os extremos.
print(frase[0:len(frase)])
print(frase[:])

#Posso percorrer a string ao contrário.
print(frase[::-1])

#Para particionar ao contrario eu tenho que dizer aonde começa e termina ao contrario.
print(frase[10:3:-1]) # Ele também seque o 10 como intervalo fechado e 3 como intervalo aberto.
