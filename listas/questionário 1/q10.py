def fibonacci(n, chamadas):
    chamadas[n] += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1, chamadas) + fibonacci(n-2, chamadas)
    
n = int(input())

chamadas = [0] * (n + 1)

resultado = fibonacci(n, chamadas)

print(f"Termo: {resultado}")
print('Quantidades:')
for i in range(n + 1):
    print(f"fibonacci({i}) - {chamadas[i]}")