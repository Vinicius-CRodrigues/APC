'''
Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.

Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.
'''

vogais = 'aeiouAEIOUáéíóÁÉÍÓ'

contador = 0


texto = input('Digite um texto: ')

for i in texto:
    if i in vogais:
        contador += 1

print(f'O texto contém {contador} vogais.')

