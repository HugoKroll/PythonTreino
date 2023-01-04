from re import M
#Famoso IMC

nome = input("Qual seu nome? ")
peso = float(input("qual seu peso? "))
altura = float(input("qual sua altura? "))
sexo = input("Qual seu sexo? F ou M ")

imc = peso/(altura**2)
print (nome, " seu imc é ", imc)
if sexo == "M":
    if imc <20.7:
        print("\nAbaixo do peso")
    elif imc < 26.4:
        print("No peso normal")
    elif imc <27.8:
        print("Sobrepeso")
    elif imc <31.1:
        print("Acima do peso ideal")
    else:
        print("Obeso")
elif sexo == "F":
    if imc <19.1:
        print("\nAbaixo do peso")
    elif imc < 25.8:
        print("No peso normal")
    elif imc <27.3:
        print("Sobrepeso")
    elif imc <32.3:
        print("Acima do peso ideal")
    else:
        print("Obeso")
else:
    print ("Sexo inválido")