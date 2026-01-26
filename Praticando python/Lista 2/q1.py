lista_compras = ['arroz', 'feijão', 'ovo', 'leite']

verificar_item = input('Digite o item que você quer verificar: ')


if verificar_item not in lista_compras:
    print(f'O item {verificar_item} precisa ser comprado.')
else:
    print(f'O item {verificar_item} já está na lista de compras.')

    