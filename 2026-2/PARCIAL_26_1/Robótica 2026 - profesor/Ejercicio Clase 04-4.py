import numpy as np
from rot3D import Rxh, Ryh, Rzh, Th
np.set_printoptions(suppress=True,precision=4)
H=Th(3,0,2)@Ryh(90)@Rxh(-30)
print(H)