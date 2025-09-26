class Carro: 
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f'O carro {self.modelo} acelerou para {self.velocidade} km/h')

    def desacelerar(self, freio):
        while self.velocidade > 0:
            self.velocidade -= freio
            print(f'O carro {self.modelo} desacelerou para {self.velocidade}. km/h')
            
        print(f'O carro {self.modelo} parou.')
    
# Criando os objetos de cada carro
meu_carro = Carro("Hondinha City","Cinza")
carro_instrutor = Carro("Suzuki Jimny", "Amarelo")
carro_uber = Carro("La Ferrai", "Verde")

# usando os metodos
meu_carro.acelerar (20)
meu_carro.acelerar (30)
meu_carro.desacelerar (10)
carro_uber.acelerar (5)