lista=["uno", "dos", "tres",10, 10+20, True, False, [1,2]]
print(lista)

#largo
print ("largo de lista: ", len(lista))

print ("\n\nCiclo for: ")
for i in lista:
    print (i)

i=0
print ("\n\nCiclo while: ")
while i< len(lista):
    print(lista[i])
    i=i+1


print("\n\n")

#acceder al elemento de una lista
print ("Primer elemento: ",lista[0])
print ("Ultimo elemento: ", lista[-1])
print ("Elementos entre el indice 2 y 3", lista[2:4])
print ("De la posición 0 a la 3 ", lista[:4])
print ("De la posición 4 en adelante: ", lista[4:])
print ("Un elemento de la lista interna: ", lista[-1][-1])

#ver si un elemento existe
if "dos" in lista:
    print ("El elemento existe")
else:
    print ("El elemento no existe")
    

#modificar un elemento
lista[0]="Elemento 1"

#modificar un rango de elementos
lista[1:3] =["Elemento 2","Elemento 3"]

#Agregar elementos (posición, valor)
lista.insert(0,"nuevo")

#Agregar al final
lista.append("Ultimo")

print (lista)

#eliminar elementos por valor
lista.remove("Elemento 2")

#eliminar elemento por indice, si no se coloca indice elimina el último
lista.pop(0)

print(lista)

#vaciar lista
lista.clear()
print (lista)

lista2=[250,300,1,8,25,4]
lista2.sort()
print ("Orden ascendente: ",lista2)

lista2.sort(reverse = True)
print ("Orden descendente: ",lista2)

#eliminar lista por completo, de memoria
del lista

conjunto ={1,4,2,3,8,1,2}
print("tamaño de conjunto", len(conjunto))
print ("Conjunto ", conjunto)


listax=[]
for i in range(6):
    listax.append(input("ingrese un nombre: ")) 


listax.sort()
print (listax)
