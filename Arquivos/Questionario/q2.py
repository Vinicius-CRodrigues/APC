nome_arquivo = input()

with open (nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read().replace(',', ';')

print(conteudo)

