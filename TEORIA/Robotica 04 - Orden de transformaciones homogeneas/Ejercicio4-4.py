import numpy as np
from homo4 import *
np.set_printoptions(precision=4,suppress=True)
HAB=T4(3,0,0)@Rz4(-180)
HBC=T4(0,0,2)@Ry4(90)@Rx4(150)
HAC=HAB@HBC
print(HAC)