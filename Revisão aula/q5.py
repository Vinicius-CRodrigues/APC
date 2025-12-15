pessoas = {
    "Ana": 25,
    "Bruno": 30,
    "Carla": 22,
    "Diego": 28,
    "Eduarda": 19,
    "Felipe": 32,
    "Gabriela": 27,
    "Hugo": 35,
    "Isabela": 21,
    "João": 40,
    "Karla": 24,
    "Lucas": 29,
    "Mariana": 26,
    "Nicolas": 31,
    "Olivia": 23,
    "Paulo": 33,
    "Quezia": 20,
}

lista = list(pessoas.items())


for i in lista:
    lista.sort(key = lambda x: x[1], reverse = True)
    
termos = lista[0:10]

print
  
for nome, num in termos:
    print(f'{nome} : {num}')