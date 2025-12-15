primeira_vez = True
menor_preco = 0 
menor_peixe = ''
contador = 0

while True:
    peixe, preco = input().split()

    preco = float(preco)

    if  peixe == 'fim' and preco < 0:
        break

    if primeira_vez == True:
        menor_preco = preco
        menor_peixe = peixe
        primeira_vez = False
    else:
        if preco < menor_preco and preco > -1:
            menor_preco = preco
            menor_peixe = peixe
    

    contador += 1

if contador == 0:
    print('Não tem')
else:
    print(f'| {menor_peixe:<19}| R$ {menor_preco:>19.2f} |')


