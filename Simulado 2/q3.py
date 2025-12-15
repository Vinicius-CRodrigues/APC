n, i = input().split()
n = int(n)
i = int(i)


matriz = []

for j in range(n):
    elemento = input().split()
    matriz.append(elemento)


for h in range(n):
    matriz[i - 1][h], matriz[h][i - 1] = matriz[h][i - 1], matriz[i - 1][h]


for linha in matriz:
    print(*linha)

'''
TESTE:
3 3
4 5 6
7 8 9
3 2 1
'''