'''
Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:

Pedra ganha de Tesoura (Pedra quebra Tesoura);
Tesoura ganha de Papel (Tesoura corta Papel);
Papel ganha de Pedra (Papel cobre Pedra);
Se ambos escolherem a mesma opção, é um empate.
'''

import random as rd

opcoes = ['pedra', 'papel', 'tesoura']

humano = input('Escolha: pedra, papel ou tesoura? ')

computador = rd.choice(opcoes)

print(f'O computador escolheu {computador}.')

if humano == 'pedra' and computador == 'tesoura':
    print('Você venceu!')
elif humano == 'tesoura' and computador == 'papel':
    print('Você venceu!')
elif humano == 'papel' and computador == 'pedra':
    print('Você venceu!')
elif humano == computador:
    print('Empate!')
else:
    print('Você perdeu!')
