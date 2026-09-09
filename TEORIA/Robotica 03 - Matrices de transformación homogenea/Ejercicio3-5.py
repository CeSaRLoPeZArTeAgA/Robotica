import numpy as np
from homo4 import *
np.set_printoptions(precision=4,suppress=True)

H = Rx4(53) @ T4(5,6,7)
r_xyz = np.array([2,3,4,1])
rp_xyz = H @ r_xyz
rp_xyz = rp_xyz[:3]

print("H = \n",H)
print("r_xyz = ",rp_xyz)