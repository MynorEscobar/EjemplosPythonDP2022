
from tkinter import Button, Label, Tk

ventana3 = Tk()
ventana3.title("Ventana 3")
ventana3.geometry("300x500")
fuente = ("arial",16)

lbl_titulo = Label(ventana3,text="Ventana 3", font=("arial",20))
btn_principal = Button(ventana3,text="regresar", font=fuente)


lbl_titulo.pack()
btn_principal.pack()

ventana3.mainloop()