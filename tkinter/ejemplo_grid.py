import tkinter

fuenteElementos = ("Arial", 18)

def sumar():
    resultado =  float(txt_valor1.get()) + float(txt_valor2.get())
    lbl_resultado["text"]= resultado

def restar():
    resultado =  float(txt_valor1.get()) - float(txt_valor2.get())
    lbl_resultado["text"]= resultado
    
def multiplicar():
    resultado =  float(txt_valor1.get()) * float(txt_valor2.get())
    lbl_resultado["text"]= resultado
    
def dividir():
    resultado =  float(txt_valor1.get()) / float(txt_valor2.get())
    lbl_resultado["text"]= resultado

ventana = tkinter.Tk()
ventana.geometry()
ventana.title("Ejemplo Grid")

lbl_titulo = tkinter.Label(ventana, text="Ejemplo Grid", font=("Arial",30), bg="red")

lbl_valor1 = tkinter.Label(ventana, text="Valor 1", font= fuenteElementos)
txt_valor1 = tkinter.Entry(ventana, font= fuenteElementos)

lbl_valor2 = tkinter.Label(ventana, text="Valor 2", font= fuenteElementos)
txt_valor2 = tkinter.Entry(ventana, font= fuenteElementos)

btn_suma = tkinter.Button(ventana, text="+", font= fuenteElementos, bg="green", command= sumar)
btn_resta = tkinter.Button(ventana, text="-", font= fuenteElementos, bg="green", command= restar)
btn_multi = tkinter.Button(ventana, text="*", font= fuenteElementos, bg="green", command= multiplicar)
btn_divi = tkinter.Button(ventana, text="/", font= fuenteElementos, bg="green", command= dividir)

lbl_resultado = tkinter.Label(ventana, text="Resultado", font= fuenteElementos)

#posiciones en el sistema GRID
lbl_titulo.grid(row=0, column=0, columnspan=4, sticky=(tkinter.W,tkinter.E))
lbl_valor1.grid(row=1, column=0)
txt_valor1.grid(row=1, column=1, columnspan=3)

lbl_valor2.grid(row=2, column=0)
txt_valor2.grid(row=2, column=1, columnspan=3)

btn_suma.grid(row=3, column=0, sticky=(tkinter.W, tkinter.E) )
btn_resta.grid(row=3, column=1, sticky=(tkinter.W, tkinter.E))
btn_multi.grid(row=3, column=2, sticky=(tkinter.W, tkinter.E))
btn_divi.grid(row=3, column=3, sticky=(tkinter.W, tkinter.E))

lbl_resultado.grid(row=4, column=0, columnspan=4, sticky=(tkinter.W, tkinter.E))

ventana.mainloop()