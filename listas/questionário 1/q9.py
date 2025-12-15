
m, n = map(int, input().split())


matriz = []
maior_distancia = 0

for i in range(m):
    linha_str = input().split()
    linha = []
    for valor in linha_str:
        linha.append(int(valor))
    matriz.append(linha)




for fila in matriz:
    posicao_pessoas = []
    for i in range(len(fila)):
        if fila[i] == 1:
            posicao_pessoas.append(i)
            
    melhor_cadeira = 0

    for i in range(n):
        if fila[i] == 0: 
            menor_distancia = 0 
            for p in posicao_pessoas:
                distancia = abs(i - p)
                if menor_distancia == 0 or distancia < menor_distancia:
                    menor_distancia = distancia
                    
            if menor_distancia > melhor_cadeira:
                melhor_cadeira = menor_distancia
    
    if melhor_cadeira > maior_distancia:
        maior_distancia = melhor_cadeira


print(maior_distancia)