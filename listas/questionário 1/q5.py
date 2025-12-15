def paron(lista):
    vogais = 'aeiouAEIOU'
    resultado = []

    for palavra in lista:
        soma_vogais = 0  
        for letra in palavra:
            if letra in vogais:
                soma_vogais += 1
        if soma_vogais % 2 == 0:  
            resultado.append(palavra)

    return resultado