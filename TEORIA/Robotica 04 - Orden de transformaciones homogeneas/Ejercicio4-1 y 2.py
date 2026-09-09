import numpy as np
from homo4 import *
np.set_printoptions(precision=4,suppress=True)
H=T4(3,3,3)@Rz4(90)@Rx4(-90)
print(H)
############
print()
H=Rx4(-90)@Ry4(-90)@T4(2,-1,0)@T4(-2,-2,-2)@T4(3,0,-1)
print(H)
##################
print()
H=Rz4(90)@T4(0,-3,2)@Rx4(-90)@T4(3,-1,0)
print(H)