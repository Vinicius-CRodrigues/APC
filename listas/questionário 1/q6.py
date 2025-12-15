lista = input()

lista = lista.split()

lista = list(map(int, lista))

f1, f2 = input().split()

f1, f2 = int(f1), int(f2)


nova_lista = lista[f1:f2]

print(nova_lista)