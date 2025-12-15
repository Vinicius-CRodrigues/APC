def palindromo_string(frase: str) -> bool:
    return frase == frase[::-1]

def palindromo(frase):
    #Substituindo os espaços em branco por nada com o replace.
    frase = frase.replace(' ', '')
    return frase.lower() == frase[::-1].lower()

def busca_string(frase, string):
    #Retorna quantas vezes string ocorre em frase com o método find.
    contador = 0 
    position = -1
    
    while True:
        position = frase.find(string, position + 1)
        if position == -1:
            return contador
        else:
            contador += 1

def busca_palavra(frase, palavra):
    #Conta quantas vezes palavra ocorre em frase.
    letras_validas = 'abcdefghijklmnopqrstuvwxyz'
    cont = 0
    palavra_aux = ''
    for letra in frase:
        if letra.lower() in letras_validas:
            palavra_aux += letra 
        else:
            if palavra_aux.lower() == palavra.lower():
                cont += 1
            palavra_aux = ''
    
    return cont



frase = input('Digite uma frase: ')
palavra = input('Digite uma palavra que quer buscar: ')




print(f'A frase {frase} é uma string palindromo ? {palindromo_string(frase)}')

print(f'A frase {frase} é uma frase palindromo ? {palindromo(frase)}')

print(f'A palavra {palavra} ocorre {busca_string(frase, palavra)} vezes na frase.')


print(f'A palavra {palavra} ocorre {busca_palavra(frase, palavra)} vezes na frase.')




