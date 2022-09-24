from Automovil import Automovil
class Camioneta(Automovil):
    #atributos
    capacidadCarga=0.0
    #metodos
    def verDatosCamioneta(self):
        print("Capacidad de carga ", self.capacidadCarga ," litros" )