'''
Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.

Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.
'''

lista_compras = ['arroz', 'feijão', 'ovo', 'leite']

verificar_item = input('Digite o item que você quer verificar: ')


if verificar_item not in lista_compras:
    print(f'O item {verificar_item} precisa ser comprado.')
else:
    print(f'O item {verificar_item} já está na lista de compras.')

