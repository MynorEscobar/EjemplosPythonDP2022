print("Valores del 0 al 9")
for i in range(10):
    print (i)

print("\n\n\nValores del 1 al 10")
for i in range(1,11):
    print (i)

print("\n\n\nValores del 1 al 10, con incremento 2")
for i in range(1,11,2):
    print (i)

print("\n\n\nValores del 1 al 10, con incremento 3 y mensaje de finalización del ciclo")
for i in range(1,11,3):
    print (i)
else:
    print ("Ciclo finalizado")


print("\n\n\nBreak")
for i in range(1,11):
    if i>3:
        break
    print (i)
else:
    print("Finalizado")

print("\n\n\nContinue")
for i in range(1,11):
    if i==3 or i==4:
        continue
    print (i)

print("\n\nRecorrer un texto")
texto="Guatemala"         
for letra in texto:
    print (letra)


print("\n\nImprimir una lista")
lista = [1,2,3,4,5]         
for i in lista:
    print (i)

print("\n\nListas anidadas")
lista1 = ["uno", "dos", "tres"]
lista2 = [1,2,3,4]

for x in lista1:
  for y in lista2:
    print(x, y)


    
