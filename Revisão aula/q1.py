# Quantas vezes o 8 aparece em numeros de 1 a 100.

list_count_8 = [str(n).count('8') for n in range (1, 101)]

total = sum(list_count_8)

print(total)
    
    