#-*- CODING UDF-8 -*-

from math import sqrt
from math import pow
import matplotlib.pyplot as plt

def segundoGrau(b, a, c):
    return (b**2)-(4*a*c)


resp = 0

while resp <= 1:
    a=float(input("Digite o valor para A: "))
    b=float(input("Digite o valor para B: "))
    c=float(input("Digite o valor para C: "))

    d=segundoGrau(b,a, c)

    try:
        e=sqrt(d)
        x1=(-b-e)/2
        x2=(-b+e)/2
        print("-"*15)
        print("X1 = "+str(x1))
        print("X2 = "+str(x2))
        print("-"*15)
        plt.plot(d)
        plt.show()
    except Exception as e:
        #print(e)
        print(e)

    resp = int(input("Voce quer continuar? (1.Sim ou 2.Nao) "))
