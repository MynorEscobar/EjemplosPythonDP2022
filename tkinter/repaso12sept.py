import tkinter

ventana = tkinter.Tk()
ventana.title = "Repaso"
ventana.geometry("300x500")

fuenteControles = ("Arial","12")

def hola():
    lbl_nombre["text"] = "Ejemplo"
    lbl_apellido["text"] = "12/09/2022"

lbl_titulo = tkinter.Label(ventana, text="Repaso", font=("Times New Roman","24"))
txt_nombre = tkinter.Entry(ventana, font=fuenteControles)
lbl_nombre = tkinter.Label(ventana, text="Nombre", font=fuenteControles)
lbl_apellido = tkinter.Label(ventana, text="Apellido", font=fuenteControles, bg="red")
btn_ver = tkinter.Button(ventana, text="Ver datos", command=hola)

lbl_titulo.pack()
txt_nombre.pack(fill=tkinter.X)
lbl_nombre.pack()
lbl_apellido.pack(fill=tkinter.X)
btn_ver.pack()


ventana.mainloop()

