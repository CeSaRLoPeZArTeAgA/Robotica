import numpy as np
from rot3D import Rxh, Ryh, Rzh, Th
np.set_printoptions(suppress=True,precision=4)
H01=Th(0,1,0)@Th(0,0,1)@Ryh(90)@Rzh(90)
H12=Th(0.5,0.1,-0.5)@Rzh(90)@Rxh(90)
H23=Th(1.9,0,0)@Ryh(-90)
print("H01")
print(H01)
print("H02")
H02=H01@H12
print(H02)
print("H03")
H03=H02@H23
print(H03)
print("H23")
print(H23)
print("H32")
H32=np.linalg.inv(H23)
print(H32)


