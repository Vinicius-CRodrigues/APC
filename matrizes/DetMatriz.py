#Percorrendo as diagonais de uma matriz:
'''
Para percorrermos a diagonal de uma matriz ela precisa ser quandrática:
A quantidade de linhas precisa ser igual a quantidade de colunas.
matriz[i][j] i == j

3x3(i.j):
[
    [0.0, 0.1, 0.2],
    [1.0, 1.1, 1.2],
    [2.0, 2.1, 2.2]
]
Analisando a diagonal principal percebemos que o indice i é igual ao j
Logo, usaremos condicionais dentro do for para conferir a diagonal principal.
'''

def criaMatriz(coluna, linha):
    matriz = []
    for i in range(coluna):
        line = list(range(i, i + linha))
        matriz.append(line)
    return matriz

def mostraMatriz(colunas):
    for linha in colunas:
        for cols in linha:
            print(cols, end=' ')
        print()
        

matriz = criaMatriz(5, 5)

mostraMatriz(matriz)

indice = 0

# pegando as diagonais principais.
while indice < len(matriz):
    print(matriz[indice][indice])
    indice += 1 

print()

# Pegando a diagonal secundaria.
linha = 0
tamanho = len(matriz)
coluna = tamanho - 1

while linha < tamanho:
    print(matriz[linha][coluna])
    linha += 1
    coluna -= 1
    


    
               

