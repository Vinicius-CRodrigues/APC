lista_1 = []
lista_2 = []
mean = []

for i in range(5):
    num_1 = int(input())
    
    lista_1.append(num_1)
    
    
for j in range(5):
    num_2 = int(input())
    
    lista_2.append(num_2)
    
concatena = list(zip(lista_1, lista_2))

for h in concatena:
    media = sum(h) / len(h)
    
    mean.append(media)
    
print(concatena)
print(mean)