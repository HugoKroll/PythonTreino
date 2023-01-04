
# Biblioteca de funções criadas por
# José Ricardo - Aula dia 08/06/2022
# atualizada aula dia 15/06/2022
import math

def fat(n) -> int:
    f = 1
    for k in range(2,abs(n)+1):
        f *= k
    return f

def permutacao(n) -> int:
    return fat(n)

def arranjo(n,p) -> int:
    return fat(n) / fat(n-p)

def combinacao(n,p) -> int:
    return fat(n) / (fat(p) * fat(n-p))

def converterEmRadianos(angulo) -> float:
    return angulo / 180.0 * math.pi

def converterEmGraus(angulo) -> float:
    return angulo * 180.0 / math.pi

def reducaoAo1Quadrante(angulo) -> float:
    angulo = angulo % 360
    quadrante = 1
    if (90 < angulo <= 180):
        angulo = 180 - angulo
        quadrante = 2
    elif (180 < angulo <= 270):
        angulo = angulo -180
        quadrante = 3
    elif (angulo>270):
        angulo = 360 - angulo
        quadrante = 4
        
    return [angulo, quadrante]    

#Calcula seno de ângulo em Graus
def seno(angulo) -> float:
    sinal = 1
    ang1Q = reducaoAo1Quadrante(angulo)
    angRad = converterEmRadianos(ang1Q[0])
    if (ang1Q[1]>2):
        sinal = -1
        
    soma = 0
    #for i in range(0,7):
    #    soma = soma + (-1)**i * angRad**(2*i+1) / fat(2*i+ 1)
    
    erro = 1
    i = 0
    while erro > 10**-9:
        termo = (-1)**i * angRad**(2*i+1) / fat(2*i+ 1)
        soma = soma + termo
        i += 1
        #print(i)
        erro = abs(termo)
    
    
    return sinal * soma
    
#Calcula cosseno de ângulo em Graus
def cosseno(angulo) -> float:
    sinal = 1
    ang1Q = reducaoAo1Quadrante(angulo)
    angRad = converterEmRadianos(ang1Q[0])
    if (1<ang1Q[1]<4):
        sinal = -1
        
    soma = 0
    for i in range(0,7):
        soma = soma + (-1)**i * angRad**(2*i) / fat(2*i)
    
    return sinal * soma
    
#Calcula tangente de ângulo em Graus    
def tangente(angulo) -> float:
    return seno(angulo) / cosseno(angulo)

#Calcula cotangente de ângulo em Graus    
def cotangente(angulo) -> float:
    return cosseno(angulo) / seno(angulo)

#Calcula secante de ângulo em Graus    
def secante(angulo) -> float:
    return 1.0 / cosseno(angulo)

#Calcula cossecante de ângulo em Graus    
def cossecante(angulo) -> float:
    return 1.0 / seno(angulo)

# esse método será utilizado para ordenar um vetor
def ordenarVetor(v , ordem):
    # 1 = crescente
    # 2 = descrecente
    col = len(v)
    for k in range(0,col-1):
        for j in range(k+1,col):
            if  v[k]> v[j] and ordem == 1:
                v[k] = v[k] + v[j]
                v[j] = v[k] - v[j]
                v[k] = v[k] - v[j]
            elif v[k] < v[j] and ordem == 2:
                v[k] = v[k] + v[j]
                v[j] = v[k] - v[j]
                v[k] = v[k] - v[j]
    return v  

def somaVetor(v) -> float:
    col = len(v)
    soma = 0
    for k in range(0,col):
        soma += v[k]
    return soma
    
    
def mediaVetor(v) -> float:
    return somaVetor(v) / len(v)

def crieMatriz(n_linhas, n_colunas, valor):
    matriz = [] 
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz

def crieVetor(n_linhas, valor):
    matriz = [] 
    for i in range(n_linhas):
        matriz.append(valor)
    return matriz

def crieMatriz3D(n_x, n_y, n_z, valor):
    matriz = [] 
    for i in range(n_x):
        linha = []
        for j in range(n_y):
            profund = []
            for k in range(n_z):
                profund.append(valor)
            linha.append(profund)
        matriz.append(linha)
    return matriz

def escalonarMatriz2D(M):
    linha = len(M)
    coluna = len(M[0])
    for i in range(linha-1):
        if (M[i][i] != 0):
            for k in range(i+1,linha):
                fator = - M[k][i] / M[i][i]
                for j in range(i,coluna):
                    M[k][j] = M[i][j] * fator + M[k][j]
        else:
            for k in range(i+1,linha):
                if (M[k][i]!=0):
                    troca = M[k]
                    M[k] = M[i]
                    M[i] = troca
                    i -= 1
                    k = linha
    return M

def resolverSistemaLinear(M):
    M = escalonarMatriz2D(M)
    #print(M)
    linha = len(M)
    coluna = len(M[0])
    linhaNula = 0
    #Matriz R armazenará as linhas não nulas da matriz M
    R = []
    for i in range(linha):
        todos = True
        for k in range(coluna):
            if (M[i][k]!=0):
                todos = False
                k = coluna
        if (todos == False):
            R.append(M[i])
    
    linha = len(R)          
    if (coluna == linha + 1 and R[linha-1][coluna-2] !=0):
        v = crieVetor(linha,0)
        for k in range(linha-1,-1,-1):
            v[k] = R[k][coluna-1]
            for i in range(coluna-2,k,-1):
                v[k] = v[k] - R[k][i]*v[i]
            v[k] = v[k] / R[k][k]
        return v
    else:
        return "Falta implementar!"    

#calcular determinante
def calculaDeterminante(M):
    M=escalonarMatriz2D
    det=1
    for i in range(0,len(M)):
        det *= M[i][i]
    return det