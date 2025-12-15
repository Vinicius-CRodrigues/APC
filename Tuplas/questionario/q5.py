def stockmarket(stock):
    
    dicionario = {}
    
    for data, valor, qtd, simb in stock:
        
        if data in dicionario.keys():
            dicionario[data] += float(valor * qtd)
        else:
            dicionario[data] = float(valor * qtd)
        
    return dicionario

stock = [('25-Out-2020', 40.0, 100, 'GM'),
('25-Out-2020', 42.0, 100, 'FIT'),
('01-Nov-2020', 36, 100, 'GM'),
('01-Nov-2020', 20, 100, 'FIT')]
print(stockmarket(stock))