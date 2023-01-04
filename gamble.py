#Programa que calcula o "lucro" ao fazer uma aposta onde se ganha 3x o valor apostado e é vitoria quando os numeros do dado de 6 lados são iguais 
import random
saldo = 1000
print ("Saldo inicial: ", saldo)
for i in range(0,1000):
  die_1 = random.randint(1, 6)
  die_2 = random.randint(1, 6)
  if die_1 == die_2:
    saldo += 4
  else:
    saldo -1
    #apresenta apenas o saldo final
print ("Saldo final: ", saldo)