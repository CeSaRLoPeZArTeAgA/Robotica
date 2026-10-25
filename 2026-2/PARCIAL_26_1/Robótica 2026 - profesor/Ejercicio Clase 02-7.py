import numpy as np
from rot3D import Rx,Ry,Rz
v=np.array([2,3,4])
R=Rz(-60)@Ry(30)@Rx(45)
v_r=R@v
print(v_r)
