def fib(n):
    n1 = 0
    n2 = 1
   
    for f in range(n):
        print(n1)
        n1, n2 = n2, n1 + n2
    

num = int(input('Digite um numero'))

fib(num)

def divisor(n):
    def dividendo(m):
        return m/n
    return dividendo

div = divisor(2)

print(div(10))

