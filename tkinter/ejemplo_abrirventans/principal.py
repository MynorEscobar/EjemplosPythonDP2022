from tkinter import Button, Label, Tk

ventana = Tk()
ventana.title("Principal")
ventana.geometry("300x500")
fuente = ("arial",16)

def abrirVentana1():
    import ventana1

def abrirVentana2():
    import ventana2

def abrirVentana3():
    import ventana3
    

lbl_titulo = Label(text="Menú Principal", font=("arial",20))
btn_ventana1 = Button(text="Ventana 1", font=fuente, command=abrirVentana1)
btn_ventana2 = Button(text="Ventana 2", font=fuente, command=abrirVentana2)
btn_ventana3 = Button(text="Ventana 3", font=fuente, command=abrirVentana3)

lbl_titulo.pack()
btn_ventana1.pack()
btn_ventana2.pack()
btn_ventana3.pack()

ventana.mainloop()