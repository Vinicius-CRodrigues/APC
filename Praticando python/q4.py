'''
Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.

Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.
'''


texto = input('Digite um texto: ')

lista = texto.split()

lista_longa = []

for i in lista:
    if len(i) > 10:
        lista_longa.append(i)

if len(lista_longa) == 0:
    print('Nenhuma palavra longa foi encontrada no texto. ')
else:
    print(' '.join(lista_longa))







