import numpy as np
from homo4 import *
np.set_printoptions(precision=4,suppress=True)
HAB=T4(0,4,2)@Rx4(-90)@Ry4(-180)
HBC=T4(3,0,0)@Rx4(-90)@Rz4(143.1)
HAC=HAB@HBC
print(HAC)