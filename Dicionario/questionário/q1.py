frase = input().lower()


contagem = {}

letras = ['d', 'v', 't']

for letra in letras:
    contador = frase.count(letra)

    if contador > 0:
        contagem[letra] = contador


for key, value in contagem.items():
    print(key, value)

