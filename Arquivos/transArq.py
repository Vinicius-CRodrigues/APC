arquivo = 'andorinha.txt'

novo_arquivo = 'andorinha_invertida.txt'


with open(arquivo, 'r') as arquivo_leitura:
    texto = arquivo_leitura.read()


palavra = input('Digite a palavra que deseja inverter: ')

if palavra in texto:
    palavra_invertida = palavra[::-1]

    texto_modificado = texto.replace(palavra, palavra_invertida)


with open(novo_arquivo, 'w') as arquivo_escrita:
    arquivo_escrita.write(texto_modificado)


