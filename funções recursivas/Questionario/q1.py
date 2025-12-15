def imprimeTermos(n):
    if n <= 0:
        print(0)
        return 0
    else:
        print(n)
        imprimeTermos(n - 2)


imprimeTermos(15)