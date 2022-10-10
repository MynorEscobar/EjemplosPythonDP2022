
from tkinter import Button, Entry, Label, Tk
from tkinter.ttk import Combobox
#utilizar la clase Solucion
from Solucion1 import Solucion1

ventana = Tk()
ventana.title("Ejemplo ComboBox")
ventana.geometry("400x500")
#establecer el tipo y tamaño de fuente para los diversos controles
fuente = ("Arial","18")

combo1 = Combobox()

#instanciar Solucion1
sol1 = Solucion1()
def cargarTabla():
    #asignar al atributo valor1 el contenido del contro txt_valor1
    sol1.valor1 = int(txt_valor1.get())
    #asignar al combo los valores de la lista generada en la clase
    combo1["font"]= fuente
    combo1["values"]= sol1.generarTabla()    

lbl_titulo = Label(ventana, text="Ejemplo ComboBox", font=("Arial","24"))
lbl_valor1 = Label(ventana, text="Ingrese un valor entero", font=fuente)
txt_valor1 = Entry(ventana,font=fuente)
btn_generar_tabla = Button(ventana, text="Generar Tabla", font=fuente, command=cargarTabla)



lbl_titulo.pack(pady=5)
lbl_valor1.pack(pady=5)
txt_valor1.pack(pady=5)
btn_generar_tabla.pack(pady=5)
combo1.pack(pady=5)

ventana.mainloop()
