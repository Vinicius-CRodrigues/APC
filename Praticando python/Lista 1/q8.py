'''
Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, visualizar e remover tarefas de uma lista.

Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. Use uma lista para armazenar as tarefas.
'''
lista_tarefas = []

def adicionar_tarefa(tarefa):
    lista_tarefas.append(tarefa)

def visualizar_tarefas():
    contar = 0
    for i in lista_tarefas:
        contar += 1
        print(f'{contar}. {i}')

def remover_tarefa(tarefa):
    lista_tarefas.remove(tarefa)

while True:
    print('#' * 30)
    print('1. Adicionar tarefa')
    print('2. Visualizar tarefas')
    print('3. Remover tarefa')
    print('4. Sair')
    print('#' * 30)

    opcao = int(input('Digite a opção desejada: '))

    if opcao < 1 or opcao > 4:
        print('Erro: Opção inválida! Escolha uma opção entre 1 e 4.')

    match opcao:
        case 1:
            tarefa = input('Digite a tarefa: ')
            adicionar_tarefa(tarefa)
            print('tafera adicionada !')
        case 2:
            visualizar_tarefas()
        case 3: 
            try:
                tarefa = input('Digite a tarefa a ser removida: ')
                remover_tarefa(tarefa)
                print('Tarefa removida!')
            except:
                print('Erro: Tarefa não encontrada!')
    if opcao == 4:
        print('Saindo do gerenciador de tarefas. Até mais!')
        break

