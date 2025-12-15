def escada(n):
    if n > 1:
        escada(n-1)
    print('#' * n)

escada(6)