import numpy as np
from fquad import *
np.set_printoptions(precision=4,suppress=True)
#Parte a
Q1=Rot(np.array([1,0,1]),np.pi/4*180/np.pi)
print("Q1=",Q1)
#Parte b
Q2=Rot(np.array([1,1,0]),np.pi/6*180/np.pi)
print("Q2=",Q2)
#Multiplicar los Q
Q=qprod(Q2,Q1)
print("Q=",Q)
#Convertimos a H
H=q2h(Q)
print(H)
#Definiendo el vector para H
p=np.array([1,1,1,1])
p1=H @ p
print(p1)
#Calculando con el cuaternio
p=np.array([0,1,1,1])
p1=qprod(qprod(Q,p),qconj(Q))
print(p1)



