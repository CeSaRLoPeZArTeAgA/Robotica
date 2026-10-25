import numpy as np
from rot3D import Rxh, Ryh, Rzh, Th
np.set_printoptions(suppress=True,precision=4)
Hab=Rxh(-90)@Ryh(-180)@Th(0,-2,-4)
Hbc=Th(3,0,0)@Rxh(-90)@Rzh(143.1)
H=Hab @ Hbc
print(H)
