def convert(lista):
    
    dicionario = {}
    
    for chave, valor in lista:
        if chave not in dicionario:
            dicionario[chave] = []
            
        dicionario[chave].append(valor)
            
    return dicionario

l = [(3, 91), (4, 69), (1, 85), (1, 96), (1, 7), (4, 94)]
resposta = convert(l)
print(resposta)