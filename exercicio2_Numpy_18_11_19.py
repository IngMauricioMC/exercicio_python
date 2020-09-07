#-*- CODING UDF-8 -*-

from math import sqrt
from math import pow
import matplotlib.pyplot as plt
import numpy as np

resp = 0
while resp <= 1:
    a=float(input("Digite o valor para A: "))
    b=float(input("Digite o valor para B: "))
    c=float(input("Digite o valor para C: "))

    r=b**2
    d=r-(4*a*c)

    try:
        e=sqrt(d)
        x1=(-b-e)/2
        x2=(-b+e)/2
        print("-"*15)
        print("X1 = "+str(x1))
        print("X2 = "+str(x2))
        print("-"*15)
        plt.plot([x1,x2])
        plt.show()
        arrX = np.arange(x1, x2, 20)
        plt.plot(arrX)
        print(arrX)
    except Exception as e:
        #print(e)
        print(e)

    resp = int(input("Voce quer continuar? (1.Sim ou 2.Nao) "))
