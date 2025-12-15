n, m = map(int, input().split())

matriz = []

dicionario = {}

for estados in range (m * n):
    estado, municipio, pop = input().split()
    matriz.append([estado, municipio, int(pop)])


for est, mun, pop in matriz:
    if est not in dicionario:
        dicionario[est] = pop
    else:
        dicionario[est] = max(dicionario[est], pop)

maior_valor = max(dicionario.values())

maior_pop = [chave for chave, valor in dicionario.items() if valor == maior_valor]

organizado = maior_pop.sort()

print(maior_pop[0])

'''
TESTE:
2 2
RJ rj 22
RJ vr 16
BA sa 7 
BA ps 12
'''

