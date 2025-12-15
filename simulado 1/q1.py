pessoas, tipo = input().split()
pessoas = int(pessoas)

if tipo == 'c' or tipo == 'C':
    conoa = pessoas * 60 
    print(f'Para transportar {pessoas} passageiros de canoa sairá R$ {conoa:.2f}.')
elif tipo == 'v' or tipo == 'V':
    voadora = pessoas * 120
    print(f'Para transportar {pessoas} passageiros de voadeira sairá R$ {voadora:.2f}.')
elif tipo == 'b' or tipo == 'B':
    barco = (pessoas * 40) + (pessoas * 65)
    print(f'Para transportar {pessoas} passageiros de barco sairá R$ {barco:.2f}.')


