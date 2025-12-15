frase = input()
palavra_oculta = input()

if palavra_oculta in frase:
    frase = frase.replace(palavra_oculta, "*")
    print(frase)
else:
    print('tudo certo :)')






