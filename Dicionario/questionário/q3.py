dados = input().split()

produtos = {}

for i in range(0, len(dados), 2):
    nome_produto = dados[i]
    preco = dados[i+1]
    preco = float(preco)
    produtos[nome_produto] = preco
    
dados_pedido = input().split()


valor = 0

for j in range(0, len(dados_pedido), 2):
    produto_escolhido = dados_pedido[j]
    quantidade = dados_pedido[j+1]
    quantidade = int(quantidade)
    
    valor += produtos[produto_escolhido] * quantidade
    
print(f'R$ {valor:.2f}')

