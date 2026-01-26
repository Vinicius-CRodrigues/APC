'''
Uma escola está organizando os dados dos alunos para criar um relatório resumido. Cada aluno tem seus dados registrados em uma única entrada, incluindo nome, idade e nota final no semestre. Esses dados devem ser exibidos separadamente para cada aluno no formato abaixo:

Aluno: Nome
Idade: Idade
Nota: Nota
'''

dados = input('Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ').split(',')

for i in range(0, len(dados), 3):
    nome = dados[i]
    idade = dados[i + 1]
    nota = dados[i + 2]

    print(f'Nome: {nome} \nIdade: {idade} \nNota: {nota}')