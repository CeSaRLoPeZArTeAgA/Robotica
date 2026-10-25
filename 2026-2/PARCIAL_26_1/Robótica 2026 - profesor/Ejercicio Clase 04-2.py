import numpy as np
from rot3D import Rxh, Ryh, Rzh, Th
np.set_printoptions(suppress=True,precision=4)
print("Primero H12")
H12=Th(3,0,2)@Rzh(90)
print(H12)
print("Primero H23")
H23=Th(3,0,1)@Rxh(-90)
print(H23)
print("Finalmente")
H=H12@H23
print(H)