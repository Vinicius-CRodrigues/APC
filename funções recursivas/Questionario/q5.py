def simples():
    
    repete = input()
    
    if repete != 'repete':
        return
    
    print('Olá! Vamos repetir!')
    simples()
    
simples()