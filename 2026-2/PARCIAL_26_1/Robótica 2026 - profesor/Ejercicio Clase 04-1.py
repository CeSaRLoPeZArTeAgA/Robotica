import numpy as np
from rot3D import Rxh, Ryh, Rzh, Th
np.set_printoptions(suppress=True,precision=4)
#r_uvw=np.array([-3,4,-11,1])
#r_xyz=H@r_uvw
print("Parte a: fijo")
H=Th(3,3,3)@Rxh(-90)@Ryh(-90)
print(H)
print("Parte b: movil")
H=Th(3,3,3)@Rxh(-90)@Ryh(-90)
print(H)