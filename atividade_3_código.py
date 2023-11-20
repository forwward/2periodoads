class Monitor:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho

    def exibir_informacoes(self):
        print(f'Monitor {self.marca}, Tamanho: {self.tamanho} polegadas')


class Computador:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.monitor = None  # Inicialmente, o computador não tem um monitor conectado

    def conectar_monitor(self, monitor):
        self.monitor = monitor
        print(f'Monitor {monitor.marca} conectado ao computador {self.marca} {self.modelo}.')

    def exibir_informacoes(self):
        print(f'Computador {self.marca} {self.modelo}')
        if self.monitor:
            self.monitor.exibir_informacoes()
        else:
            print('Sem monitor conectado.')


monitor1 = Monitor(marca='Dell', tamanho=27)


computador1 = Computador(marca='HP', modelo='Pavilion')


computador1.conectar_monitor(monitor1)


computador1.exibir_informacoes()
