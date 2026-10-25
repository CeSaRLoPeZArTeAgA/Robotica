import numpy as np
from rot3D import Rxh, Ryh, Rzh, Th
np.set_printoptions(suppress=True,precision=4)
Hab=Rzh(180)@Th(-3,0,0)
Hbc=Ryh(90)@Rxh(150)@Th(-2,0,0)
H=Hab @ Hbc
print(H)
