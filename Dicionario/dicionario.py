'''
Os dicionários são estruturas fechadas de dados baseadas em chave e valor. As chaves são informações inutáveis que identificam não só por posição, mas também pela sua identidade.
A sintaxe dos dicionários são entre chaves identificando a chave e o valor:

dicionario = {
'chave' : 'valor'
}
ou 
dicionario = dict(
chave = 'valor'
)
'''
# Foi criado uma lista com chaves frutas e valor o peso delas

frutas = {
    "Maçã": 150,
    "Banana": 120,
    "Laranja": 200,
    "Uva": 5,
    "Morango": 15,
    "Manga": 350,
    "Abacaxi": 1500,
    "Pêra": 180,
    "Melancia": 4000,
    "Pêssego": 100
}

#Para identificar o peso (valor) de uma fruta específica eu faço nome_dicionario[chave']:

print(f'Peso da fruta banana: {frutas['Banana']}g')

# Para adicionar um elemento na lista ou para atualizar o valor de uma chave que já existe fazemos:
frutas['Pitaya'] = 300
# Também posso usar o método update:
frutas.update({'Graviola' : 2000})

# Mudando o valor de Pêra:
frutas["Pêra"] = 170

print('Dicionario após adicionar mais uma fruta:')

print(frutas)

# Para conferir se a chave existe gento do dicionário usamos a função get:
# Caso a chave não esteja cadastrada, o programa da a resposta none.

tem_fruta = input('Digite o nome de uma fruta para conferir se ela está cadastrada: ')

if frutas.get(tem_fruta) == None:
    print(f'A fruta {tem_fruta} não está no dicionário')
else:
    print(f'A fruta {tem_fruta} está no dicionário')


# Para deletar um termo que está no dicionário utilizamos o método del:

deletar_fruta = input('Digite o nome de uma fruta para deletar: ')

del frutas[deletar_fruta]

print(f'Dicionario após deletar a fruta {deletar_fruta}:')

print(frutas)

print()

# Para conferir se aquele valor pertence a chave fazemos:
print(f'O valor 4000 está presente em alguma chave ? {4000 in frutas.values()}. E a chave Laranja está presente no dicionário ? {'Laranja' in frutas.keys()}')

# Para acessar chaves e valores com iteráveis eu faço:
print()
print('Mostrando as chaves e valores do dicionário:')
for key, value in frutas.items():
    print(f'Chave: {key} valor: {value}')

# Criando uma lista telefonica com dicionários dentro de dicionários:


lista_telefonica = {
    1 : {
        'Nome' : 'Vinicius',
        'Telefone' : '(61)99593-6553'
    },

    2 : {
        'Nome' : 'Adileuza',
        'Telefone' : '(61)98220-5701'
    }
}
print('Acessando os contatos da lista telefonica: ')

for key_lista, value_lista in lista_telefonica.items():
    print(f'Contato {key_lista}:')
    for nome, numero in value_lista.items():
        print(f'{nome}: {numero}')




