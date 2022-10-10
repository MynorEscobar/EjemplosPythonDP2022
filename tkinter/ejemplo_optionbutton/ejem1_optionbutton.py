from tkinter import *
import tkinter
from tkinter import messagebox

ventana = Tk()
ventana.title("Ejemplo ComboBox")
ventana.geometry("600x400")
#establecer el tipo y tamaño de fuente para los diversos controles
fuente = ("Arial","14")

#variable para genero
genero = tkinter.StringVar()
#establecer el genero seleccionado por defecto
genero.set('h')


#variable para estado civil
estCivil = tkinter.IntVar()
estCivil.set(1)


def seleccionarOpciones():
    print("Genero: " + genero.get())
    print("Estado Civil: " + str(int(estCivil.get())))
    messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message= "Genero: " + genero.get() + ", Estado Civil: " + str(int(estCivil.get()))
    )

lbl_titulo = Label(
    ventana, 
    text="Ejemplo Botones de Opción", 
    font=("Arial",20))

#Genero
lbl_genero = Label(ventana, text="Genero", font=fuente)
opt1_genero = Radiobutton(ventana,text="Hombre",variable=genero,value="h", font=fuente)
opt2_genero = Radiobutton(ventana,text="Mujer",variable=genero,value="m", font=fuente)

#Estado Civil
lbl_estcivil = Label(ventana, text="Estado Civil", font=fuente)
opt1_estcivil = Radiobutton(ventana,text="Soltero(a)",variable=estCivil,value=1, font=fuente)
opt2_estcivil = Radiobutton(ventana,text="Casado(a)",variable=estCivil,value=2, font=fuente)
opt3_estcivil = Radiobutton(ventana,text="Viudo(a)",variable=estCivil,value=3, font=fuente)
opt4_estCivil = Radiobutton(ventana, text="Divorciado(a)", variable=estCivil, value=4, font=fuente)


btn_selecionar = Button(ventana, text="Ver elemento selecionado", command=seleccionarOpciones, font=fuente)


lbl_titulo.grid(row=1,column=1, columnspan=5)
#posición genero
lbl_genero.grid(row=2, column=1)
opt1_genero.grid(row=2, column=2)
opt2_genero.grid(row=2, column=3)

#posición estado civil
lbl_estcivil.grid(row=3, column=1)
opt1_estcivil.grid(row=3, column=2)
opt2_estcivil.grid(row=3, column=3)
opt3_estcivil.grid(row=3, column=4)
opt4_estCivil.grid(row=3, column=5)


btn_selecionar.grid(row=4, column=1, columnspan=5)


ventana.mainloop()