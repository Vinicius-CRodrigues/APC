def mediana_e_mais_proximo_media_e_pos(lista):
    if len(lista) == 0:
        return [None, None, None]

    lista_ordenada = sorted(lista)
    tam = len(lista_ordenada)

    if tam % 2 == 0:
        mediana = (lista_ordenada[tam//2 - 1] + lista_ordenada[tam//2]) / 2
    else:
        mediana = lista_ordenada[tam//2]

    somador = sum(lista)
    media = somador / tam

    prox_media = lista[0]
    index = 0
    menor_delta = abs(lista[0] - media)

    for i, valor in enumerate(lista):
        delta = abs(valor - media)
        if delta < menor_delta:
            menor_delta = delta
            prox_media = valor
            index = i

    return [mediana, prox_media, index]