# 1. Os números 0 e 1 representados como numerais de Church. Ou seja, esses números devem ser representados como funções (ou lambdas).
ZERO = lambda f : lambda x: x
UM = lambda f : lambda x: f(x)

# 2. Os dez primeiros números primos representados como numerais de Church. Note que esses números também devem ser representados como funções.
DOIS = lambda f : lambda x: f(f(x))
TRES = lambda f : lambda x: f(f(f(x)))
CINCO = lambda f : lambda x: f(f(f(f(f(x)))))
SETE = lambda f : lambda x: f(f(f(f(f(f(f(x)))))))
ONZE = lambda f : lambda x: f(f(f(f(f(f(f(f(f(f(f(x)))))))))))
TREZE = lambda f: lambda x: f(f(f(f(f(f(f(f(f(f(f(f(f(x)))))))))))))
DEZESSETE = lambda f: lambda x: f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(x)))))))))))))))))
DEZENOVE = lambda f: lambda x: f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(x)))))))))))))))))))
VINTEETRES = lambda f: lambda x: f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(x)))))))))))))))))))))))
VINTEENOVE = lambda f: lambda x: f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(x)))))))))))))))))))))))))))))

church_to_bool = lambda f: f(True)(False)

# O operador identidade:
def identidade(n):
    return n

# O operador de adicao:
def adicao(n):
    return lambda m: n(sucessor)(m)

# O operador subtracao:
def subtracao(n):
    return lambda m: m(predecessor)(n)

# O operador multiplicacao:
def multiplicacao(n):
    return lambda m: lambda f: n(m(f))

# O operador de exponenciacao:
def exponenciacao(n):
    return lambda m : m(n)

# O operador fatorial:
def fatorial(n):
    valor = church_to_int(n)
    
    fatorial = UM
    for i in range(1, valor + 1):
        fatorial = multiplicacao(fatorial)(int_to_church(i))
    
    return fatorial

# O operador sucessor:
def sucessor(n):
    return lambda f: lambda x: f(n(f)(x))

# O operador predecessor:
def predecessor(n):
    return (lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda u: x)(lambda u: u))

# A função church_to_int 
def church_to_int(n):
    return n(lambda x: x + 1)(0)

# A função int_to_church:
def int_to_church(n):
    resultado = ZERO
    for i in range(n):
        resultado = sucessor(resultado)

    return resultado

# O operador is_zero:
def is_zero(n):
    true = lambda x: lambda y: x
    false = lambda x: lambda y: y

    return n(lambda m: false)(true)

def leq(n):
    return lambda m: is_zero(subtracao(n)(m))

def geq(n):
    return lambda m: is_zero(subtracao(m)(n))