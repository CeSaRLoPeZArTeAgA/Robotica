import numpy as np
from homo4 import *
np.set_printoptions(precision=4,suppress=True)
H01=T4(0,1,1)@Rx4(90)@Ry4(90)
H12=T4(0.5,0.1,-0.5)@Ry4(90)@Rz4(90)
H23=T4(1.9,0,0)@Ry4(-90)
print("H01")
print(H01)
print("H02")
print(H01@H12)
print("H03")
H03=H01@H12@H23
print(H03)
print("H23")
print(H23)
