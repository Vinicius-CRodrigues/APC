'''
cebolinhar:
Fazer uma frase ser igual a forma que o cebolinha fala.
r = l
R = L
rr = l 
RR = L
'''
def cebolinhar(frase):
    ultima_letra_r = False
    nova_frase = ''

    for letra in frase:
        if letra == 'r':
            if not ultima_letra_r:
                nova_frase += 'l'
                ultima_letra_r = True
            letra = 'l'
        elif letra == 'R':
            if not ultima_letra_r:
                nova_frase += 'L'
                ultima_letra_r = True
            letra = 'L'
        else:
            nova_frase += letra 
            ultima_letra_r = False 
        

    return nova_frase

def cebolinhar_2(frase):
    frase = frase.replace('rr', 'l')
    frase = frase.replace('RR', 'L')
    frase = frase.replace('r', 'l')
    frase = frase.replace('R', 'L')
    return frase


frase = input('Digite uma frase: ')

print(cebolinhar(frase))
print(cebolinhar_2(frase))
print(frase)

