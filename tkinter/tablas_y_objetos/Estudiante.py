class Estudiante:
    #atributos
    carnet=0
    nombre=""
    apellido=""
    telefono=""
    
    #metodos
    def verDatos(self):
        print ("Carnet: " , self.carnet, " nombre: ", self.nombre, " apellido: ", self.apellido,  " telefono:", self.telefono)
        #print ("Carnet: %d, nombre: %s, apellido: %s, telefono: %s" %(self.carnet, self.nombre, self.apellido, self.telefono))
    