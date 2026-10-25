import numpy as np
from rot3D import Rxh, Ryh, Rzh, Th
np.set_printoptions(suppress=True,precision=4)
H=Th(1,2,0)@Rzh(45)
r_uvw=np.array([2,4,6,1])
r_xyz=H@r_uvw
r_xyz=r_xyz[:3]
print (r_xyz)