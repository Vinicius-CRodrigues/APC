'''
O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.

Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?
'''

lista_corredores = ['Ana', 'João', 'Pedro']

incorreto = input('Digite o nome incorreto: ')

correto = input('Digite o nome correto: ')

posicao = lista_corredores.index(incorreto)

lista_corredores[posicao] = correto

print(lista_corredores)

