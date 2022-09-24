import tkinter
from tkinter import *
from tkinter import ttk
from Estudiante import Estudiante

#crear ventana 
ventana = Tk()
ventana.title = "Ejemplo tablas y objetos"
ventana.geometry("500x500")

tabla = ttk.Treeview(ventana, columns=("col1","col2","col3"))

#instanciar la clase para asignar valores a los atributos y utilizar los métodos

listaEstudiante = []
    
def guardaDatos():
    estudiante = Estudiante()
    #asignar los valores a los atributos
    estudiante.carnet = int(txt_carnet.get())
    estudiante.nombre = txt_nombre.get()
    estudiante.apellido = txt_apellido.get()
    estudiante.telefono = txt_telefono.get()
    #agregando el estudiante a la lista
    listaEstudiante.append(estudiante)
    generarTabla()
    limpiarCajasTexto()
    
'''-------------------------------------------------------      
def verDatos():
    estudiante.verDatos()
---------------------------------------------------------'''
def generarTabla():
    #limpiar o borrar las filas antes de cargar de nuevo
    for fila in tabla.get_children():
        tabla.delete(fila)
        
    #establecer el tamaño de las columnas
    tabla.column("#0", width=125)
    tabla.column("col1", width=125)
    tabla.column("col2", width=125)
    tabla.column("col3", width=125)
    
    tabla.heading("#0", text="Carnet", anchor=CENTER)
    tabla.heading("col1", text="Nombre", anchor=CENTER)
    tabla.heading("col2", text="Apellido", anchor=CENTER)
    tabla.heading("col3", text="Telefono", anchor=CENTER)
    
    #ciclo para pasar los elementos de lista de estudiantes
    for registro in listaEstudiante:
        tabla.insert("",END, text=registro.carnet, values=(registro.nombre, registro.apellido, registro.telefono))
    
    tabla.pack(fill= tkinter.X)
def limpiarCajasTexto():
    #borrar el contenido de los controles Entry
    txt_carnet.delete(0,"end")
    txt_nombre.delete(0,"end")
    txt_apellido.delete(0,"end")
    txt_telefono.delete(0,"end")
    #pone el foco a este elemento
    txt_carnet.focus_set()
    
fuente = ("Arial", 16)

lbl_titulo = Label(ventana, text="Ejemplo de tablas y objetos", font=("Arial","20"))

lbl_carnet = Label(ventana, text="Carnet:", font = fuente)
txt_carnet = Entry(ventana, font= fuente)

lbl_nombre = Label(ventana, text="Nombre:", font = fuente)
txt_nombre = Entry(ventana, font= fuente)

lbl_apellido = Label(ventana, text="Apellido:", font = fuente)
txt_apellido = Entry(ventana, font= fuente)

lbl_telefono = Label(ventana, text="Telefono:", font = fuente)
txt_telefono = Entry(ventana, font= fuente)

btn_guardar = Button(ventana, text="Guardar datos", command=guardaDatos, font=fuente)



lbl_titulo.pack()
lbl_carnet.pack(anchor = tkinter.W)
txt_carnet.pack(fill = tkinter.X)

lbl_nombre.pack(anchor = tkinter.W)
txt_nombre.pack(fill = tkinter.X)

lbl_apellido.pack(anchor = tkinter.W)
txt_apellido.pack(fill = tkinter.X)

lbl_telefono.pack(anchor = tkinter.W)
txt_telefono.pack(fill = tkinter.X)

btn_guardar.pack(fill = tkinter.X)




ventana.mainloop()

 