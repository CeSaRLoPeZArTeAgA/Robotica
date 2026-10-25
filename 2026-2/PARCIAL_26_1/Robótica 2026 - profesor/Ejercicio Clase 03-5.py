import numpy as np
from rot3D import Rxh, Ryh, Rzh, Th
np.set_printoptions(suppress=True,precision=4)
H=Rxh(53)@Th(5,6,7)
r_xyz=np.array([2,3,4,1])
r_prima=H@r_xyz
print(r_prima)