n = int(input())

matriz = []
principal= []
principal_upper = []
secundaria = []

for i in range(n):
    elementos = input().split()
    matriz.append(elementos)
    


indice = 0
linha = 0
tamanho = len(matriz)
coluna = tamanho - 1

while indice < tamanho:
    principal.append(matriz[indice][indice])
    
    indice += 1

while linha < tamanho:
    secundaria.append(matriz[linha][coluna])
    linha += 1
    coluna -= 1
    
    
for s in principal:
    principal_upper.append(s.upper())
        
if principal_upper == secundaria and 'O' not in principal_upper:
    print('O one piece eh real!')
else:
    print('Talvez o tesouro seja os amigos que fizemos no caminho')
    
    
