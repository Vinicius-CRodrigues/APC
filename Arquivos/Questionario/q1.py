nome_arquivo = input()

with open (nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read().replace('\n', ' ').lower()

polystation = ''.join(sorted('polystation'))
nintendo = ''.join(sorted('nintendomeiaquatro'))

if polystation in conteudo:
    print('o poderoso polystation ainda vive')

else:
    print('O encanador venceu outra vez')

