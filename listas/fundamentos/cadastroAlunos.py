'''
Cadastro de notas de alunos com listas.

'''

def menu():
    while True:
        print('Opções:')
        print('1.Cadastra aluno: ')
        print('2.Inserir notas: ')
        print('3. Ver notas: ')

        operacao = int(input('Digite a opção desejada: '))
        if 1 <= operacao <= 3:
            return operacao

def efetua_cadastro(cadastro):
    '''
    Função que cadastra os dados de um aluno e inicializa as notas das listas e projetos com [0.0]
    '''
    nome = input('Digite o nome do aluno: ')
    sobrenome = input('Digite o nome do aluno: ')
    matricula = input('Digite a matrícula do aluno: ')
    notas_listas = [0.0] * 11 #Crio uma lista com 11 prosições e as notas inicializadas em 0.0.
    notas_projetos = [0.0] * 3 #Crio uma lista com 3 posições e inicializo com 0.0.
    cadastro.append([nome, sobrenome, matricula, notas_listas, notas_projetos]) #Uso o append para incluir itens na lista, que no caso é uma nova lista

def entrada_notas(cadastro):
    '''
    Função que busca um aluno no cadastro e solicita a entrada de notas das listas e projetos.
    '''
    if len(cadastro) == 0:
        print('Não há alunos cadastrados. Cadastre um aluno.')
    else:
        matricula = input('Digite a matrícula do aluno: ')
        achou = False
        for aluno in range (len(cadastro)):
            if cadastro[aluno][2] == matricula:
                achou = True
                print(f'Entre com as notas do {cadastro[aluno][0]} {cadastro[aluno][1]}')

                for listas in range(len(cadastro[aluno][3])):
                    cadastro[aluno][3][listas] = float(input(f'Digite a nota da lista {listas + 1}: '))

                for projetos in range(len(cadastro[aluno][4])):
                    cadastro[aluno][4][projetos] = float(input(f'Digite a nota do projeto {projetos + 1}: '))
                break

        if not achou:
            print(f'Matricula {matricula} não encontrada.')       
                
def extrato(cadastro):
    '''
    Função que imprime as notas individuais de cada aluno, as médias e a nota final de cada aluno.
    '''
    for extrato in range (len(cadastro)):
        print(f'{cadastro[extrato][0]} {cadastro[extrato][1]}')
        for listas in range(len(cadastro[extrato][3])):
            print(f'Lista {listas + 1}: {cadastro[extrato][3][listas]}')
        for projetos in range(len(cadastro[extrato][4])):
            print(f'Projeto {projetos + 1}: {cadastro[extrato][4][projetos]}')
        media_listas = sum(cadastro[extrato][3]) / len(cadastro[extrato][3])
        media_projetos = sum(cadastro[extrato][4]) / len(cadastro[extrato][4])
        media_final = (media_listas + media_projetos) / 2
        print(f'Média das listas: {media_listas}')
        print(f'Média dos projetos: {media_projetos}')
        print(f'Média final: {media_final}')




cadastro = []

continua = 's'

while continua != 'n':
    operacao = menu()

    if operacao == 1:
        efetua_cadastro(cadastro)
    if operacao == 2:
        entrada_notas(cadastro)
    if operacao == 3:
        extrato(cadastro)

    continua = input('Deseja continuar? (s/n): ')
   