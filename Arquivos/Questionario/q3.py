pedido = input().lower()


lista = []
custo = 0

with open('cardapio.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        
        nome, preco = linha.split('/')
    
        if pedido == nome.lower():
            lista.append([nome, float(preco)])
            custo += float(preco)

if lista:
    for nome, preco in lista:
        print(f'{nome} {preco:.2f}')
    print(f'Sua conta deu: {custo:.2f}')
else:
    print('Infelizmente não temos este prato')
