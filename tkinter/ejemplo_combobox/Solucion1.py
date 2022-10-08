class Solucion1:
    #atributos
    valor1=0
    
    #métodos
    def generarTabla(self):
        lista = []
        #range(valor inicial, valor final - 1)
        for i in range(1,11):
            lista.append(str(i) + " X " + str(self.valor1) + " = " + str (i * self.valor1))
        return lista
    