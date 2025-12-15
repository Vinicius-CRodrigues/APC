n = int(input())

compras = {}
sep = ', '

for i in range(1, n+1):
    itens = input().split()
    produtos = []
    
    for j in range(0, len(itens), 2):
        fruta = itens[j]
        preco = float(itens[j+1])
        
        produtos.append([fruta, preco])
    
    compras[i] = produtos

    
corredor = int(input())

if corredor not in compras:
    print('Esse corredor não existe no mercado.')

else:
    produtos = compras[corredor]
    
    frutas = [produto[0] for produto in produtos]
    preco = [produto[1] for produto in produtos]
    
    media = sum(preco) / len(preco)
    frutas_sep = sep.join(frutas)
    
    print(f'No corredor {corredor} encontramos:')
    print(frutas_sep)
    print(f'E o preço médio é {media:.2f}.')