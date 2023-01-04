razao = float(input("Razao da PA: "))
pt = float(input("Primeiro termo da PA: "))
nt = float(input("Numero de termos da PA: "))
ut = pt+(nt-1)*razao
print("último termo: "+str(ut))
print("Soma total: "+str(((pt+ut)*nt)/2))