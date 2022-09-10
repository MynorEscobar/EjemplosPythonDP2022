#Crear una aplicacion con GUI con Python para realizar las 4 operaciones básicas(+,-,*,/) con 2 numeros
import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x500")

fuenteTitulo = ("Arial Black",24)
fuenteElmentos = ("Arial",18)
resultado = 0.0

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
    

lbl_titulo = tkinter.Label(ventana, text="Calculadora Básica", bg="gray", font= fuenteTitulo)
#fill = tkinter.X abarcar todo el ancho
lbl_titulo.pack(fill = tkinter.X)

lbl_valor1 = tkinter.Label(ventana, text="Valor 1", font= fuenteElmentos)
lbl_valor1.pack(fill = tkinter.X, pady=3)
txt_valor1 = tkinter.Entry(ventana, font= fuenteElmentos)
txt_valor1.pack(fill = tkinter.X, pady=3)

lbl_valor2 = tkinter.Label(ventana, text="Valor 2", font= fuenteElmentos)
lbl_valor2.pack(fill = tkinter.X, pady=3)
txt_valor2 = tkinter.Entry(ventana, font= fuenteElmentos)
txt_valor2.pack(fill = tkinter.X, pady=3)

btn_suma = tkinter.Button(ventana, text="Suma", font= fuenteElmentos, bg="green", command= sumar)
btn_suma.pack(fill = tkinter.X, pady=3)

btn_resta = tkinter.Button(ventana, text="Resta", font= fuenteElmentos, bg="green", command= restar)
btn_resta.pack(fill = tkinter.X, pady=3)

btn_multi = tkinter.Button(ventana, text="Multiplicar", font= fuenteElmentos, bg="green", command= multiplicar)
btn_multi.pack(fill = tkinter.X, pady=3)

btn_divi = tkinter.Button(ventana, text="Dividir", font= fuenteElmentos, bg="green", command= dividir)
btn_divi.pack(fill = tkinter.X, pady=3)

lbl_resultado = tkinter.Label(ventana, text="Resultado", font= fuenteElmentos)
lbl_resultado.pack(fill = tkinter.X, pady=3)


ventana.mainloop()