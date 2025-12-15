n = int(input())

notas = {}
lista = []

for i in range(n):
    nome, nota = input().split(',')
    nota = float(nota)

    notas[nome] = nota

nota_aluno = float(input())

for key, value in notas.items():
    if nota_aluno == value:
        lista.append(key)
    
if nota_aluno not in notas.values():
    print('Você foi o único aluno com essa nota.')

nova_lista = sorted(lista)
separador = '/'

resultado = separador.join(nova_lista)

print(resultado)
