import numpy as np
from rot3D import Rxh, Ryh, Rzh, Th
np.set_printoptions(suppress=True,precision=4)
H=Th(3,2,4)@Ryh(53)@Rxh(60)@Rzh(45)
print (H)