from classes import Computador, Tela

host = Computador('lenovo', '8gb', '1tb', 'i5')
host.ligar()
host.exibir_configurações()

monitor = Tela('15.6 polegadas', '1920x1080', 'Samsung')
monitor.ligar()
monitor.exibir_configurações()

host.desligar()
monitor.desligar()