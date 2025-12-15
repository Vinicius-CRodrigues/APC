#Calcular as raízes de uma função quadratica ax^2 + bx + c = 0

'''
1. Ler os valores de a, b e c fornecidos pelo usuário
2. Calcular as raízes da função quadrática.
3. Imprimir as raízes calculadas.

Para calcular as raizes:
Delta: b^2 - 4ac
raiz 1 = (-b + sqrt(delta)) / 2a
raiz 2 = (-b - sqrt(delta)) / 2a
raiz 3 = Não há raiz real.
raiz 4 = delta igual a zero = -b / 2a

'''
#Criando as funções:
def calcula_delta(a, b, c):
    return b**2 - 4*a*c

def calcula_x1(a, b, delta):
    return (-b + delta**0.5) / (2*a)

def calcula_x2(a, b, delta):
    return (-b - delta**0.5) / (2*a)

def calcula_zero(a, b):
    return -b / (2*a)


def calcular_raizes(a, b, c):
    delta = calcula_delta(a, b, c)

    if delta > 0 :
        raiz_1 = calcula_x1(a, b, delta)
        raiz_2 = calcula_x2(a, b, delta)
        print(f'raiz 1 = {raiz_1} e raiz 2 = {raiz_2}')

    elif delta == 0:
        raiz_zero = calcula_zero(a, b)
        print(f'raiz = {raiz_zero}')

    else:
        print('Não há raízes reais.')



#Entrada de dados:
print('Vamos calcular a função ax^2 + bx + c = 0')

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

print()
calcular_raizes(a, b, c)
