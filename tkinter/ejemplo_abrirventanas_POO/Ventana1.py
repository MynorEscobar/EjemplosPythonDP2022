import tkinter
class Ventana1:
    #atributos la ventana y los controles
    ventana1 = tkinter
    fuente = ("arial",16)
    lbl_titulo = tkinter.Label
    btn_principal = tkinter.Button
        
    #metodos
    def construirVentana(self):
        self.ventana1 = tkinter.Tk()
        self.ventana1.title("Ventana 1")
        self.ventana1.geometry("300x500")
        self.lbl_titulo = tkinter.Label(self.ventana1,text="Ventana 1", font=("arial",20))
        self.btn_principal = tkinter.Button(self.ventana1,text="Hola", font=self.fuente, command=self.decirHola)
        self.lbl_titulo.pack()
        self.btn_principal.pack()    
        self.ventana1.mainloop()
        
    def decirHola(self):
        print("Hola mundo")