def nota(N):
    preenchida = '★'
    vazia = '☆'
    print(f'|{preenchida * N}{vazia * (10 - N)}|')