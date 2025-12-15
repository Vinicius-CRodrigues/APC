linha = int(input())

with open('/etc/passwd', 'r') as arquivo:
    linhas = arquivo.readlines()


print(linhas[linha - 1].split(':')[0])

