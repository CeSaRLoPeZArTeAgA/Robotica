import numpy as np
from rot3D import Rxh, Ryh, Rzh, Th
np.set_printoptions(suppress=True,precision=4)
print("Parte a: P respecto a 1")
p2=np.array([0,2,1,1])
H12=Th(3,0,2)@Rzh(90)
p1=H12@p2
print(p1[:3])
print("Parte b: P respecto a 3")
H23=Th(3,0,1)@Rxh(-90)
p3=np.linalg.inv(H23)@p2
print(p3[:3])
print("Parte b: P respecto a 3 ")
H32=Th(-3,1,0)@Rxh(90)
p3=H32@p2
print(p3[:3])