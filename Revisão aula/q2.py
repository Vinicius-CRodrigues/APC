digito, inicio, fim = input().split()

inicio, fim = int(inicio), int(fim)

list_count_8 = [str(n).count(str(digito)) for n in range (inicio, fim + 1)]

total = sum(list_count_8)

print(total)