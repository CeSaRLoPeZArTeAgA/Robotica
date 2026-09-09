import numpy as np
from homo4 import *
np.set_printoptions(precision=4,suppress=True)
H=T4(3,0,2)@Ry4(90)@Rx4(-30)
print(H)