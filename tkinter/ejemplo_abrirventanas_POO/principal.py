from tkinter import Button, Label, Tk
from Ventana1 import Ventana1 
from Ventana2 import Ventana2

ventana = Tk()
ventana.title("Principal")
ventana.geometry("300x500")
fuente = ("arial",16)


def abrirVentana1():
    #crear un objeto de tipo ventana y llamar al metodo que construye la ventana 
    vent1 = Ventana1()
    vent1.construirVentana()
    print("hola")
    
def abrirVentana2():
    vent2 = Ventana2()
    vent2.crearVentanan2()

def abrirVentana3():
    import ventana3
    

lbl_titulo = Label(text="Menú Principal", font=("arial",20))
btn_ventana1 = Button(ventana, text="Ventana 1", font=fuente, command=abrirVentana1)
btn_ventana2 = Button(ventana, text="Ventana 2", font=fuente, command=abrirVentana2)
btn_ventana3 = Button(ventana, text="Ventana 3", font=fuente, command=abrirVentana3)

lbl_titulo.pack()
btn_ventana1.pack()
btn_ventana2.pack()
btn_ventana3.pack()

ventana.mainloop()