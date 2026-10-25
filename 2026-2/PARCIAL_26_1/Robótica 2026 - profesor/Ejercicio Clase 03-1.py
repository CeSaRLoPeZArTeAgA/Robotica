import numpy as np
from rot3D import Rzh, Th
np.set_printoptions(suppress=True,precision=4)
H=Th(2,3,0)@Rzh(45)
print (H)

