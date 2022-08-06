conjunto = {"a","e","i",10,20,"a","e",10,20,10}

print (conjunto)
print ("Largo :" , len(conjunto))
print ("Tipo de elemento: ", type(conjunto)) #tipo set = conjunto

print ("\n\nlistar elementos del conjunto:")
for elemento in conjunto:
    print(elemento)
    
print("\n\nVerificar si un elemento existe en el conjunto")
print ("10 existe en el conjunto: ", 10 in conjunto)
print ("45 existe en el conjunto: ",45 in conjunto)

#Agregar elementos al conjunto
print("\n\nAgregar elementos al conjunto:")
conjunto.add(45)
conjunto.add(11*3)
print (conjunto)

print("\n\nSolicitar 5 textos y almacenarlos en un conjunto")
#iniciar un conjunto vacio
conjuntoTextos =set(())
for i in range(6):
    conjuntoTextos.add(input("Ingrese un texto: "))

print("\n\nLista de elementos del conjunto")
for elemento in conjuntoTextos:
    print(elemento)
