inicio, fim = input().split()

inicio, fim = int(inicio), int(fim)

for digito in range(0 , 10):
    list_count = [str(n).count(str(digito)) for n in range (inicio, fim + 1)]

    total = sum(list_count)

    print(digito, ':', total )