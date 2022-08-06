
valEntero = int(input("Ingrese un número entero: "))
valTexto = input("ingrese un texto: ")
valBooleano = bool(input("Ingrese un booleano: "))
valFloat = float(input("Ingrese un valor con decimales: "))
valCualquiera = eval(input("Ingrese un valor de cualquier tipo: "))

valBoolV = True
valBoolF = False

#type es una función para ver el tipo de datos
print ("valEntero: ",type(valEntero),": ", valEntero)
print ("valTexto: ",type(valTexto),": ", valTexto)
print ("valBooleano: ",type(valBooleano),": ", valBooleano)
print ("valFloat: ",type(valFloat),": ", valFloat)
print ("valCualquiera: ",type(valCualquiera),": ", valCualquiera)

print("Booleano Verdadero: ", valBoolV)
print("Booleano Falso: ", valBoolF)
print ("Feliz día")
