def JaChegou(n : int, frase: str):
    if n == 0:
        return 0
    
    print(frase)
    JaChegou(n - 1, frase)

JaChegou(5, 'A gente ja chegou?')