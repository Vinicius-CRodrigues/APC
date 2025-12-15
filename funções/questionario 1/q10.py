def troco(x):
    moeda = x // 50
    x = x % 50
    print(f'{moeda} moedas de 50 centavos')
    moeda2 = x // 25
    x = x % 25  
    print(f'{moeda2} moedas de 25 centavos')
    moeda3 = x // 10
    x = x % 10
    print(f'{moeda3} moedas de 10 centavos')
    moeda4 = x // 5
    x = x % 5
    print(f'{moeda4} moedas de cinco centavos')
    moeda5 = x // 1
    x = x % 1   
    print(f'{moeda5} moedas de 1 centavo')