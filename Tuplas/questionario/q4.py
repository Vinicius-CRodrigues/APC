def erase(lista):

    for i in lista[:]:
        if len(i) == 0:
            lista.remove(i)
    
    return lista

l = [(), (15,), (), (), (2, 15, 17)]
resposta = erase(l)
print(resposta)