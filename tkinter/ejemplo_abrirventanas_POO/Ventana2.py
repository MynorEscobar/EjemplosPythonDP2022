import tkinter

class Ventana2:
    #atributos 
    ventana2 = tkinter
    lblTitulo = tkinter
    txtNombre = tkinter
    btnNombre = tkinter
    lblNombre = tkinter
    fuente = ("arial",16)
    #metodos
    def crearVentanan2(self):
        #construir la ventana
        self.ventana2 = tkinter.Tk()
        self.ventana2.title("Ventana 2")
        self.ventana2.geometry("500x300")
        
        self.lblTitulo = tkinter.Label(self.ventana2, text="Ventana 2", font=("Arial",20))
        self.txtNombre = tkinter.Entry(self.ventana2, font=self.fuente)
        self.btnNombre = tkinter.Button(self.ventana2, text="Ver Nombre", command=self.verNombre, font=self.fuente)
        self.lblNombre = tkinter.Label(self.ventana2, text="nombre", font=self.fuente)

        self.lblTitulo.pack()
        self.txtNombre.pack()
        self.btnNombre.pack()
        self.lblNombre.pack()
        
        self.ventana2.mainloop()
        
    def verNombre(self):
        print(self.txtNombre.get())
        self.lblNombre["text"]=self.txtNombre.get()
            
    