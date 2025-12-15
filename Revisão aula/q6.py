nome_arquivo = input()

lista = []
dicionario = {}

with open(nome_arquivo, 'r') as arquivo_leitura:
    linhas = arquivo_leitura.readlines()

for i in linhas:
     normalizado = i.strip()
     separado = normalizado.split()


     lista.append(separado)
     
for j in lista:
    for h in j:
        if h in dicionario:
            dicionario[h] += 1
        else:
            dicionario[h] = 1

nova_lista = list(dicionario.items())

for i in nova_lista:
    nova_lista.sort(key = lambda x: x[1], reverse = True)

termos = nova_lista[0:10]

for nome, num in termos:
    print(f'{nome} : {num}')