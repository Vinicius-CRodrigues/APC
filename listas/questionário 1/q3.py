sequencia = input()
sequencia = sequencia.split()
n = int(input())

converter = []
multiplos = []

for i in sequencia:
    converter.append(int(i))
    
    
for j in converter:
    if j % n == 0:
        multiplos.append(j)

for h in multiplos:
    print(h, end=' ')