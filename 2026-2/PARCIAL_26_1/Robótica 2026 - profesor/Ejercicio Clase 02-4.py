import numpy as np
from rot3D import Rx,Ry,Rz
v=np.array([2,3,4])
R=Rz(45)@Rx(30)@Rz(-60)
v_r=R@v
print(v_r)

