'''
Jogo da forca:
Se o usuário acertar a letra, ela será preenchida, se não será eliminada.
'''
palavra_secreta = 'perfume'
letras_digitadas = []



while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue
    
    letras_digitadas.append(letra)

    if letra not in palavra_secreta:
        letras_digitadas.pop()

    temp = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_digitadas:
            temp += letra_secreta
        else:
            temp += '*'

    print(temp)

    if temp == palavra_secreta:
        print('Você completou a palavra!')
        break



