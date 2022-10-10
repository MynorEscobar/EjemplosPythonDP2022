from tkinter import Button, Entry, Label, Tk, messagebox
from tkinter.ttk import Combobox
#utilizar la clase Solucion

ventana = Tk()
ventana.title("Ejemplo ComboBox")
ventana.geometry("400x500")
#establecer el tipo y tamaño de fuente para los diversos controles
fuente = ("Arial","18")

#generar lista para cargar elemento posteriormente en un combobox
lista = []
for i in range(1,16):
    lista.append(i)

#función para seleccionar un elemento de la lista    
def selection_changed(event):
    selection = combo1.get()
    messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message=selection
    )
    
def verSeleccionado():
    messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message=combo1.get()
    )

lbl_titulo = Label(ventana, text="Ejemplo ComboBox", font=("Arial","24"))

combo1 = Combobox(
    state="readonly",
    values=lista
)
#código para llamar a la funcion selection_changed
combo1.bind("<<ComboboxSelected>>",selection_changed)

btn_selecionar = Button(ventana, text="Ver elemento selecionado", command=verSeleccionado)

lbl_titulo.pack()
#pady = para dejar margen (vertical, eje y) entre entre 2 controles
combo1.pack(pady=10)
btn_selecionar.pack()

ventana.mainloop()
