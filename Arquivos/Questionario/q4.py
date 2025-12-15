def caminho(s: str):
    try:
        with open(s, 'r') as arquivo:
            print(f'Voce esta no {s}')
    except:
        print('Apaguei?')

caminho('a.txt')
