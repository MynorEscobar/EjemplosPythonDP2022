from Vehiculo import Vehiculo
#(clase padre) = Herencia
class Automovil(Vehiculo):
    #atributos
    velocidad=0
    cc=0.0
    #metodos
    def verDatosAutomovil(self):
        print("Velocidad: ", self.velocidad, " c.c.: ", self.cc)
        