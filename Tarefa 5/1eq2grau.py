import math as m
print("Em uma equação do tipo ax²+bx+c = 0, informe: \n")
a = float(input("Quoeficiente a: "))
b = float(input("Quoeficiente b: "))
c = float(input("Quoeficiente c: "))
delta = (b**2)-(4*a*c)
if delta >0:
    x1=(-b+m.sqrt(delta))/2*a
    x2=(-b-m.sqrt(delta))/2*a
    print ("x1 =" +str(x1), " x2 = "+str(x2), " Delta positivo, eq possui 2 raizes reais")
elif delta == 0:
    x1=(-b)/(2*a)
    print ("x1 =" +str(x1), " Delta = 0, eq possui 1 raiz")
else:
    print ("Delta negativo, não possui raizes reais")