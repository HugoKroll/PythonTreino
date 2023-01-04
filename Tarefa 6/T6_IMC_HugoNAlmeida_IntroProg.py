from mailbox import NotEmptyError
from re import M

from tkinter import *
import tkinter.messagebox as mbox
##Feito por Hugo Nogueira Almeida. Intro prog, 2/8
class Janela():
    def __init__(self,root) -> None:
        self.lblNome = Label(text="Nome")
        self.lblNome.place(x=10, y=10, height=50, width=50)
        
        self.txtNome = Entry()
        self.txtNome.place(x=70, y =10, height=50, width =250)
    
        self.lblAltura = Label(text="Altura")
        self.lblAltura.place(x=10, y=70, height=50, width=50)
        
        self.txtAltura = Entry()
        self.txtAltura.place(x=70, y =70, height=50, width =50)

        self.lblPeso = Label(text="peso")
        self.lblPeso.place(x=10, y=130, height=50, width=50)
        
        self.txtPeso = Entry()
        self.txtPeso.place(x=70, y =130, height=50, width =50)

        self.selecionar = IntVar()
        self.selecionar.set(1)
        self.rdSexo = Radiobutton(text="Feminino", value=1, variable=self.selecionar)
        self.rdSexo.place(x=80,y=190, height=50, width=100)
        self.rdSexo = Radiobutton(text="Masculino", value=2, variable=self.selecionar)
        self.rdSexo.place(x=180,y=190, height=50, width=100)
        self.bttCalcular = Button(text="Calcular")
        self.bttCalcular.place(x=80, y=250, height=50, width=100)
        self.bttCalcular["command"] = self.calcimc

        self.lblIMC = Label()
        self.lblIMC.place(
            x=10,y=310, height=60,
            width=300
        )




    def calcimc(self):
    
        nome = self.txtNome.get()
        peso = float(self.txtPeso.get())
        altura = float(self.txtAltura.get())
        sexo = self.selecionar.get()
        imc = peso/(altura**2)
        mensagem = nome + ", seu imc é " + str(imc) +"\nVocê está "
        if sexo == 1:
            if imc <20.7:
                mensagem += "Abaixo do peso"
            elif imc < 26.4:
                mensagem +="No peso normal"
            elif imc <27.8:
                mensagem +="Sobrepeso"
            elif imc <31.1:
                mensagem +="Acima do peso ideal"
            else:
                mensagem +="Obeso"
        elif sexo == 2:
            if imc <19.1:
                mensagem +="\nAbaixo do peso"
            elif imc < 25.8:
                mensagem +="No peso normal"
            elif imc <27.3:
                mensagem +="Sobrepeso"
            elif imc <32.3:
                mensagem +="Acima do peso ideal"
            else:
                mensagem +="Obeso"
        else:
            mensagem +="Sexo inválido"
        self.lblIMC["text"] = mensagem
            




# iniciar a execucao
root = Tk()
root.title("Cálculo do IMC")
root.geometry("400x400")
aplicativo = Janela(root)
root.mainloop()

