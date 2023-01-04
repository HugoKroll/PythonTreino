import math as m
per = float(input("Perímetro do retangulo: "))
lado = float(input("Tamanho de um dos lados: "))
print("Diagonal do retangulo: " +str(m.sqrt(lado**2+(((lado*2)-per)/2)**2)))