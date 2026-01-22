'''
Programação Orientada a Objetos (POO) é um paradigma que organiza o código em torno de objetos, que agrupam dados (atributos) e comportamentos (métodos) para modelar entidades do mundo real, facilitando o desenvolvimento de sistemas complexos, modulares e fáceis de manter, usando princípios como Encapsulamento, Herança, Polimorfismo e Abstração. 

'''
class Computador:
    # Iniciaremos com um construtor:
    def __init__(self, marca, memoria_ram, armazenamento, processador):
        # Dentro desse construtor, eu adiciono os atributos.
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.armazenamento = armazenamento
        self.processador = processador

    # Construo métodos para essa classe.
    def ligar(self):
        print('Ligando o computador...')
    
    def desligar(self):
        print('Desligando o computador...')
    
    def exibir_configurações(self):
        print('Configurações do computador:')
        print(f'Marca: {self.marca}')
        print(f'Memória RAM: {self.memoria_ram}')
        print(f'Armazenamento: {self.armazenamento}')
        print(f'Processador: {self.processador}')

class Tela:
    def __init__(self, tamanho, resolução, marca):
        self.tamanho = tamanho
        self.resolução = resolução
        self.marca = marca

    def ligar(self):
        print('Ligando a tela...')

    def desligar(self):
        print('Desligando a tela...')
    
    def exibir_configurações(self):
        print('Configurações da tela:')
        print(f'Tamanho: {self.tamanho}')
        print(f'Resolução: {self.resolução}')
        print(f'Marca: {self.marca}')





