'''
Construiremos matrizes com listas. Então uma lista com uma sequencia de listas geram uma matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# No primeiro for eu acesso as listas que estão dentro da lista matriz.
# No segundo for eu acesso os elementos que estão dentro das listas que está na lista matriz.
print('Destacando a matriz:')
for colunas in matriz:
    for linhas in colunas:
        print(linhas, end=' ')
    print()

# Construindo matrizes:
linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))

print('Criando uma matriz com zeros:')
matriz_zeros = []
zeros = [0] * linhas

for zero in range(colunas):
    print (zeros)
    
matrix = []
interna = []


for cols in range(colunas):
    elementos = input('Digite os elementos separados por espaço: ').split()
    interna.append(elementos)


for colunas in interna:
    for linhas in colunas:
        print(linhas, end=' ')
    print()