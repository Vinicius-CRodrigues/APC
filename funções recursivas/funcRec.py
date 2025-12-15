'''
Funções recursivas são funções que retornam elas mesmas baseado em 3 casos:
CASO BASE: O caso para qual a função converge e não tem mais função.
CASO RECURSIVO: Quando a função chama ela própria
Toda vez que eu chao uma função, ela entra na pilha de chamadas com todo o seu escopo salvo na memória.

'''

def fatorial(n: int) -> int:

    # Caso base:
    if n == 1 or n == 0:
        return 1
    # Caso recursivo:
    return n * fatorial(n - 1)

print(fatorial(0))




