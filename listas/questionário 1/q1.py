qde_alunos = int(input())

lista = []

for i in range (qde_alunos):
    nome = input()
    
    lista.append(nome)
    

lista.sort(reverse = True)


for j in lista:
    print(j)