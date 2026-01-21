'''
Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais.

Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial. Exiba a senha gerada.
'''

import random as rd
import string as st


def gerador_senha(size = 12):
    maiusculas = st.ascii_uppercase
    minusculas = st.ascii_lowercase
    numeros = st.digits
    caracteres = st.punctuation

    senha = []

    todos = maiusculas + minusculas + numeros + caracteres

    for i in range(size):
        senha.append(rd.choice(todos))

    # Embaralhar
    rd.shuffle(senha)

    return ''.join(senha)

for i in range(5):
    print(gerador_senha())

