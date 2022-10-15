
from tkinter import Button, Label, Tk

ventana2 = Tk()
ventana2.title("Ventana 2")
ventana2.geometry("300x500")
fuente = ("arial",16)

lbl_titulo = Label(ventana2,text="Ventana 2", font=("arial",20))
btn_principal = Button(ventana2,text="regresar", font=fuente)


lbl_titulo.pack()
btn_principal.pack()

ventana2.mainloop()