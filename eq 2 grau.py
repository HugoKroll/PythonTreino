from tkinter import *
from tkinter import messagebox as msg
import math as math
from matplotlib import pyplot as plt
import numpy as np
#Definição da janela do programa
class Janela:
    def __init__(self, root) -> None:
        self.lblTitulo = Label(text="Resolver equações do 2 grau")
        self.lblTitulo.place(x=10,y=10,height=50,width=300)
       
        self.lblA = Label(text="a = ")
        self.lblA.place(x=10, y=80,
        width=50,height=35)
       
        self.txtA = Entry()
        self.txtA.place(x=70, y=80,
        width=50,height=35)
       
        self.lblB = Label(text="b = ")
        self.lblB.place(x=10, y=120,
        width=50,height=35)
       
        self.txtB = Entry()
        self.txtB.place(x=70, y=120,
        width=50,height=35)
       
        self.lblC = Label(text="c = ")
        self.lblC.place(x=10, y=160,
        width=50,height=35)
       
        self.txtC = Entry()
        self.txtC.place(x=70, y=160,
        width=50,height=35)
       
        self.bttCalcular = Button(
        text="Calcular")
       
        self.bttCalcular.place(
        x=10,y=200,height=40,
        width=110    
        )
       
        self.lblRaizes = Label()
        self.lblRaizes.place(
            x=10,y=240, height=60,
            width=300
        )
       
        self.bttCalcular["command"] = self.calcular
#calculo
    def calcular(self):
        try:
            a = float(self.txtA.get())
            b = float(self.txtB.get())
            c = float(self.txtC.get())
            delta = b**2 - 4*a*c
            mensagem = str(a)+"x²+"+str(b)+"x+"+str(c)
            mensagem += "\nO valor de delta é: " +str(round(delta,3))
            xv = -b/(2*a)
            x= np.linspace(xv-5,xv+5,10)
            y = [a*x**2+b*x+c]
            plt.plot(x,y, color = 'red')
            if(delta)>=0:
                x1 = (-b+math.sqrt(delta))/2*a
                x2=x1
                if delta>0:
                    x2 = (-b-math.sqrt(delta))/2*a
                mensagem = mensagem + "\n x1 = " +str(round(x1,3))
                mensagem += "\n x2 = " +str(round(x2,3))
            else:
                mensagem += "\nEssa equação não possui raiz real."
            self.lblRaizes["text"] = mensagem

        except ValueError:
            msg.showerror("Erro", " Quoeficientes\n Inválidos")
        finally:
            self.txtA.delete(0,END)
            self.txtB.delete(0,END)
            self.txtC.delete(0,END)
            self.txtA.focus()
root = Tk()
root.title("Calculo das raízes!")
root.geometry("320x400")
root.resizable(False,False)
app = Janela(root)
root.mainloop()
 

