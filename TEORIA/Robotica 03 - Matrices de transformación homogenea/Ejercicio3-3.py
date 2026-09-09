import numpy as np
from homo4 import *
np.set_printoptions(precision=4,suppress=True)

H = T4(1,2,0) @ Rz4(45)
r_uvw = np.array([2,4,6,1])
r_xyz = H @ r_uvw
r_xyz = r_xyz[:3]

print("H = \n",H)
print("r_xyz = ",r_xyz)


