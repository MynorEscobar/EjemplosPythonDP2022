
from tkinter import Button, Label, Tk

ventana1 = Tk()
ventana1.title("Ventana 1")
ventana1.geometry("300x500")
fuente = ("arial",16)

lbl_titulo = Label(ventana1,text="Ventana 1", font=("arial",20))
btn_principal = Button(ventana1,text="regresar", font=fuente)


lbl_titulo.pack()
btn_principal.pack()

ventana1.mainloop()