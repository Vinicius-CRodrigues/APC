def recomenda(tags):
    lista = []
    dicionario = {}

    for i in tags:
        for j in i:
            lista.append(j)
    
    for h in lista:
        if h in dicionario.keys():
            dicionario[h] += 1
        else:
            dicionario[h] = 1

    maior_valor = [chave for chave, valor in dicionario.items() if valor == max(dicionario.values())]

    return maior_valor

tags = [['gatos', 'musica'], ['comida', 'trendy'], ['gatos'], ['estudo'], ['musica', 'comida'], ['gatos', 'cachorro']]

print(recomenda(tags))
