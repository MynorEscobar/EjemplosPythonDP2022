#lista, tuplas, conjuntos(set), diccionarios
#Diccionario es una colección que almacena datos en pares clave y un valor.
diccionario = {
        "id":1,
        "nombre":"Soyel",
        "apellido":"Inventado",
        "telefono":12345678,
        "direccion":"zona 1 Guatemala",
        "nombre":"Otro", #sobreescribe o reemplaza el valor de la clave
        "nombre":15 #sobreescribe o reemplaza el valor de la clave
        
    }

print(diccionario)
print("\n\nDatos del diccionario por medio de la clave")
print("id: ", diccionario["id"])
print("nombre: ", diccionario["nombre"])
print("Apellido: ", diccionario.get("apellido"))

print("\n\nCantidad de elementos: ", len(diccionario))
print("\n\nTipo de dato: ", type(diccionario))

print("\n\nObtener claves")
print(diccionario.keys())
print("\n\nObtener valores")      
print(diccionario.values())
print("\n\nObtener clave,valor")
print(diccionario.items())

print("\n\nVerificar si la clave existe en el diccionario")
if "apellido" in diccionario:
    print("Clave si existe, el valor es: ", diccionario.get("apellido"))
    
else:
    print("Clave no existe")

print("\n\nModificar un elemento")
diccionario.update({"nombre":"Nuevo Nombre"})
diccionario["apellido"]="Hola"
print(diccionario)

print("\n\nAgregar elementos")
diccionario.update({"email":"inventado@mail.com"})
diccionario["edad"]=20
print(diccionario)

print("\n\nEliminar el ultimo elementos")
diccionario.popitem()
print("\n\nEliminar un elemento especifico")
diccionario.pop("telefono")
print(diccionario)

print("\n\nElementos(valores) del diccionario,ciclo for: ")
for clave in diccionario:
    print(diccionario[clave])
    
print("\n\n metodo values()")
for valores in diccionario.values():
    print(valores)

print("\n\nElementos(claves) del diccionario,ciclo for: ")
for clave in diccionario.keys():
    print(clave)

print("\n\nElementos(clave, valor) del diccionario,ciclo for: ")
for clave, valor in diccionario.items():
    print(clave, ": ", valor)


diccionarioPersona1 = {
        "id":1,
        "nombre":"Soyel",
        "apellido":"Inventado",
        "telefono":12345678
    }

diccionarioPersona2 = {
        "id":2,
        "nombre":"Otra",
        "apellido":"Persona",
        "telefono":22334455
    }
diccionarioPersona3 = {
        "id":3,
        "nombre":"Tercera",
        "apellido":"Persona",
        "telefono":66778899
    }
#diccionario ={clave:valor}
diccionarioPersonas = {
        1:diccionarioPersona1,
        2:diccionarioPersona2,
        3:diccionarioPersona3
    }


for clave,valor in diccionarioPersonas.items():
    print (clave, ": ", valor) 

print("\n\n\n")
#creación de un diccionario vacio
conjuntoPersonas={}
print("Almacenar los datos de 5 personas")

for i in range(1,6):
    persona={
        "id":i,
        "nombre":input("ingrese un nombre: "),
        "apellido":input("ingrese un apellido: ")
        }
    #diccionario{clave,valor}
    conjuntoPersonas.update({i:persona})

print("\n\nDatos almacenados:")
for clave, valor in conjuntoPersonas.items():
    print (clave, ": ", valor)


print("\n\n\n")





