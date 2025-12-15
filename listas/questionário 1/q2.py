n = int(input())

lista = []

for i in range(n):
    nome = input()
    
    lista.append(nome)
    

remover = input()
remover = remover.split()

for j in lista[:]:
    if j in remover:
        lista.remove(j)
    
for h in lista:
    print(h, end=' ')