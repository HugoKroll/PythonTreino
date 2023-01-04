from mailbox import NotEmptyError
from re import M

from tkinter import *
import tkinter.messagebox as mbox
import biblioteca as bib
class Janela():
    def __init__(self,root) -> None:
        self.lblAngulo = Label(text="Angulo (graus)")
        self.lblAngulo.place(x=50, y=30, height=30, width=100)
        
        self.txtAngulo = Entry()
        self.txtAngulo.place(x=150, y =30, height=30, width =50)
    

        self.selecionar = IntVar()
        self.selecionar.set(1)
        self.rdRazao=Radiobutton(text="Seno",value=1,variable=self.selecionar)
        self.rdRazao.place(x=30,y=100,height=50,width=100)
        self.rdRazao=Radiobutton(text="Cosseno",value=2,variable=self.selecionar)
        self.rdRazao.place(x=30,y=140,height=50,width=100)
        self.rdRazao=Radiobutton(text="Tangente",value=3,variable=self.selecionar)
        self.rdRazao.place(x=30,y=180,height=50,width=100)
        self.rdRazao=Radiobutton(text="Cossecante",value=4,variable=self.selecionar)
        self.rdRazao.place(x=30,y=220,height=50,width=100)
        self.rdRazao=Radiobutton(text="Secante",value=5,variable=self.selecionar)
        self.rdRazao.place(x=30,y=260,height=50,width=100)
        self.rdRazao=Radiobutton(text="Cotangente",value=6,variable=self.selecionar)
        self.rdRazao.place(x=30,y=300,height=50,width=100)
        self.bttCalcular = Button(text="Calcular")
        self.bttCalcular.place(x=250, y=150, height=30, width=70)
        self.bttCalcular["command"] = self.calctrig
        self.lblResult = Label()
        self.lblResult.place (x=220,y=200, height=30, width=140)

    def calctrig(self):
        angulo=float(self.txtAngulo.get())
        mensagem = ("Resultado\n")
        select = self.selecionar.get()
        if select == 1:
            mensagem += str(bib.seno(angulo))
        elif select == 2:
            mensagem += str(bib.cosseno(angulo))
        elif select == 3:
            mensagem += str(bib.tangente(angulo))
        elif select == 4:
            mensagem += str(bib.cossecante(angulo))
        elif select == 5:
            mensagem += str(bib.secante(angulo))
        elif select == 6:
            mensagem += str(bib.cotangente(angulo))
        self.lblResult ["text"] = mensagem   

    


# iniciar a execucao
root = Tk()
root.title("Calculadora Trig")
root.geometry("400x400")
aplicativo = Janela(root)
root.mainloop()