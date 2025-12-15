n = int(input())

alunos = {}

for i in range(n):
    dados = input().split()
    
    nome = dados[0]
    email = dados[1]
    notas = list(map(float, dados[2:]))
    
    media = sum(notas) / 4
    
    alunos[nome] = {
        'email': email,
        'notas' : media
        }
    
nome_aluno = input()

if nome_aluno in alunos and alunos[nome_aluno]['notas'] >= 5:
    email = alunos[nome_aluno]['email']
    mean = alunos[nome_aluno]['notas']
    print(f'Destinatário: {email}')
    print(f'O aluno {nome_aluno} foi aprovado com média {mean:.2f}.')
elif nome_aluno in alunos and alunos[nome_aluno]['notas'] < 5:
    email = alunos[nome_aluno]['email']
    mean = alunos[nome_aluno]['notas']
    print(f'Destinatário: {email}')
    print(f'O aluno {nome_aluno} foi reprovado com média {mean:.2f}.')
else:
    print(f'O aluno {nome_aluno} não está na turma.')

            
    
