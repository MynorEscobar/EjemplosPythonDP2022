import tkinter
from tkinter import *
from tkinter import ttk


ventana = Tk()
ventana.title = "Ejemplo 12/09/22"
ventana.geometry ("600x500")

lbl_titulo = Label(ventana, text="Ejemplo de Tabla con Treeview", font=("Arial","30"))
lbl_titulo.pack()

tabla = ttk.Treeview(ventana, columns=("col1","col2","col3"))
#establecer el tamaño de las columnas
tabla.column("#0", width=90)
tabla.column("col1", width=90)
tabla.column("col2", width=90)
tabla.column("col3", width=90)


tabla.heading("#0", text="Carnet", anchor=CENTER)
tabla.heading("col1", text="Nombre", anchor=CENTER)
tabla.heading("col2", text="Apellido", anchor=CENTER)
tabla.heading("col3", text="Telefono", anchor=CENTER)

lista = ("Persona 1","Apellido 1","22224444")

#establecer los valores para los registros (filas)
tabla.insert("",END, text="202212345", values=(lista))
tabla.insert("",END, text="202212346", values=("dos","Inventado 2", "33445566"))
tabla.insert("",END, text="202212347", values=("tres","Inventado 3", "44556677"))


tabla.pack(fill = tkinter.X)

ventana.mainloop()