import csv

cursos = {
    '127' : 'Bacharelado em Ciência da Computação',
    '132' : 'Arquitetura e Urbanismo',
    '136' : 'Engenharia Civil',
    '137' : 'Engenharia Elétrica',
    '139' : 'Engenharia Florestal',
    '158' : 'Licenciatura em Física',
    '159' : 'Licenciatura em Química',
    '160' : 'Licenciatura em Ciências Biológicas',
    '161' : 'Licenciatura em Matemática',
    '162' : 'Licenciatura em Língua Portuguesa'
}

licenciatura = ['158', '159', '160', '161', '162']

filename = input()
f = open(filename, 'r', encoding='latin_1', newline='')
reader = csv.reader(f, delimiter=';')

soma = 0
cont = 0
total = 0
soma_idade = 0
soma_prof = 0

primeira = True

for row in reader:

    if primeira:
        primeira = False
        continue

    curso = row[1]
    idade = int(row[2])

    total += 1
    soma_idade += idade

    # TP_PRES = 555 => fez a prova
    if row[4] == "555":
        nota = row[5].replace(',', '.')
        soma += float(nota)
        cont += 1

    # QE_I70 (coluna 10) A ou C = quer ser professor
    if curso in licenciatura and row[10] in ['A', 'C']:
        soma_prof += 1

media = soma / cont if cont > 0 else 0
media_idade = soma_idade / total

print("Relatório ENADE 2017")
print(f"Curso: {cursos[curso]}")
print(f"Total de alunos inscritos: {total}")
print(f"Total de alunos que realizaram o Enade: {cont}")
print(f"Média da idade dos alunos inscritos no ENADE: {media_idade:.2f}")

if curso in licenciatura:
    print(f"Total de alunos da licenciatura que pretendem ser professor: {soma_prof}")

print(f"Média geral dos alunos que realizaram o ENADE: {media:.2f}")

f.close()
