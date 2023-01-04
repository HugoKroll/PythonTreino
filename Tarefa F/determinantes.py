from mailbox import NotEmptyError
from re import M

from tkinter import *
from tkinter.font import BOLD
import tkinter.messagebox as mbox
import biblioteca as bib
class Janela():
    def __init__(self,root) -> None:
        self.lblAngulo = Label(text="Ordem da matriz")
        self.lblAngulo.place(x=30, y=30, height=30, width=100)
        
        self.selecionar = IntVar()
        self.selecionar.set(1)
        self.slOrdem=Radiobutton(text="2 X 2",value=1,variable=self.selecionar)
        self.slOrdem.place(x=30,y=100,height=20,width=50)
        self.slOrdem=Radiobutton(text="3 X 3",value=2,variable=self.selecionar)
        self.slOrdem.place(x=30,y=120,height=20,width=50)
        self.slOrdem=Radiobutton(text="4 X 4",value=3,variable=self.selecionar)
        self.slOrdem.place(x=30,y=140,height=20,width=50)
        self.slOrdem=Radiobutton(text="5 X 5",value=4,variable=self.selecionar)
        self.slOrdem.place(x=30,y=160,height=20,width=50)
## 2x2
        self.txt11 = Entry()
        self.txt11.place(x=100, y =100, height=20, width =30)
        self.txt12 = Entry()
        self.txt12.place(x=135, y =100, height=20, width =30)
        self.txt21 = Entry()
        self.txt21.place(x=100, y =125, height=20, width =30)
        self.txt22 = Entry()
        self.txt22.place(x=135, y =125, height=20, width =30)
##3x3
        self.txt13 = Entry()
        self.txt13.place(x=170, y =100, height=20, width =30)
        self.txt23 = Entry()
        self.txt23.place(x=170, y =125, height=20, width =30)
        self.txt31 = Entry()
        self.txt31.place(x=100, y =150, height=20, width =30)
        self.txt32 = Entry()
        self.txt32.place(x=135, y =150, height=20, width =30)
        self.txt33 = Entry()
        self.txt33.place(x=170, y =150, height=20, width =30)
##4x4
        self.txt14 = Entry()
        self.txt14.place(x=205, y =100, height=20, width =30)
        self.txt24 = Entry()
        self.txt24.place(x=205, y =125, height=20, width =30)
        self.txt34 = Entry()
        self.txt34.place(x=205, y =150, height=20, width =30)
        self.txt41 = Entry()
        self.txt41.place(x=100, y =175, height=20, width =30)
        self.txt42 = Entry()
        self.txt42.place(x=135, y =175, height=20, width =30)
        self.txt43 = Entry()
        self.txt43.place(x=170, y =175, height=20, width =30)
        self.txt44 = Entry()
        self.txt44.place(x=205, y =175, height=20, width =30)
##5x5
        self.txt15 = Entry()
        self.txt15.place(x=240, y =100, height=20, width =30)
        self.txt25 = Entry()
        self.txt25.place(x=240, y =125, height=20, width =30)
        self.txt35 = Entry()
        self.txt35.place(x=240, y =150, height=20, width =30)
        self.txt45 = Entry()
        self.txt45.place(x=240, y =175, height=20, width =30)
        self.txt55 = Entry()
        self.txt55.place(x=240, y =200, height=20, width =30)

        self.txt51 = Entry()
        self.txt51.place(x=100, y =200, height=20, width =30)
        self.txt52 = Entry()
        self.txt52.place(x=135, y =200, height=20, width =30)
        self.txt53 = Entry()
        self.txt53.place(x=170, y =200, height=20, width =30)
        self.txt54 = Entry()
        self.txt54.place(x=205, y =200, height=20, width =30)

        self.bttCalcular = Button(text="Calcular")
        self.bttCalcular.place(x=100, y=250, height=30, width=70)
        self.bttCalcular["command"] = self.calcdet
        self.lblResult = Label()
        self.lblResult.place (x=170,y=250, height=30, width=140)

    def calcdet(self):
        opc = float(self.selecionar.get())
        if opc==1:
            Mat=[[float(self.txt11.get()),float(self.txt12.get())],[float(self.txt21.get()),float(self.txt22.get())]]
        elif opc==2:
            Mat=[[float(self.txt11.get()),float(self.txt12.get()),float(self.txt13.get())],
            [float(self.txt21.get()),float(self.txt22.get()),float(self.txt23.get())],
            [float(self.txt31.get()),float(self.txt32.get()),float(self.txt33.get())]]
        elif opc==3:
            Mat=[[float(self.txt11.get()),float(self.txt12.get()),float(self.txt13.get()),float(self.txt14.get())],
            [float(self.txt21.get()),float(self.txt22.get()),float(self.txt23.get()),float(self.txt24.get())],
            [float(self.txt31.get()),float(self.txt32.get()),float(self.txt33.get()),float(self.txt34.get())],
            [float(self.txt41.get()),float(self.txt42.get()),float(self.txt43.get()),float(self.txt44.get())]]
        elif opc==4:
            Mat=[[float(self.txt11.get()),float(self.txt12.get()),float(self.txt13.get()),float(self.txt14.get()),float(self.txt15.get())],
            [float(self.txt21.get()),float(self.txt22.get()),float(self.txt23.get()),float(self.txt24.get()),float(self.txt25.get())],
            [float(self.txt31.get()),float(self.txt32.get()),float(self.txt33.get()),float(self.txt34.get()),float(self.txt35.get())],
            [float(self.txt41.get()),float(self.txt42.get()),float(self.txt43.get()),float(self.txt44.get()),float(self.txt45.get())],
            [float(self.txt51.get()),float(self.txt52.get()),float(self.txt53.get()),float(self.txt54.get()),float(self.txt55.get())]]

        self.lblResult["text"] = str(bib.calculaDet(Mat))





# iniciar a execucao
root = Tk()
root.title("Calculo de Determinantes")
root.geometry("400x400")
aplicativo = Janela(root)
root.mainloop()