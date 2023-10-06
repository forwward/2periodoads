class Carro:
 pneus = 4

def  _init_(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo

carro1 = Carro("Ford", "Fiesta")
carro2 = Carro("Honda", "Civic")

print(carro1.pneus)
print(carro2.pneus)

print (Carro.pneus)