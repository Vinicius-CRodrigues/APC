def numero(num):
    num = num.replace('zero', '0')
    num = num.replace('um', '1')
    num = num.replace('dois', '2')
    num = num.replace('três', '3')
    num = num.replace('quatro', '4')
    num = num.replace('cinco', '5')
    num = num.replace('seis', '6')
    num = num.replace('sete', '7')
    num = num.replace('oito', '8')
    num = num.replace('nove', '9')

    return num 


frase = input()

print(numero(frase))