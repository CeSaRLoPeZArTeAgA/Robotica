import numpy as np
from homo4 import *
np.set_printoptions(precision=4,suppress=True)
H02=T4(0.1,1.5,1.8)@Rx4(-90)
H23=T4(-0.6,-1.2,0)@Rx4(-90)@Rz4(-90)
print("H02")
print(H02)
print("H23")
print(H23)
