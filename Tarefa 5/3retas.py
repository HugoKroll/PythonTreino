import math as m
print ("Dara as equações das retas r : y = ax + b e s : y = cx + d. Forneça:\n")
a = float(input("Quoeficiente a: "))
b = float(input("Quoeficiente b: "))
c = float(input("Quoeficiente c: "))
d = float(input("Quoeficiente d: "))

angulo = m.atan((c-a)/(1+c*a))

if angulo != 0: ##Ou se a = c
    print ("são concorrentes")
elif b != d:
    print ("São paralelas")
else:
    print ("São concorrentes")