import numpy as np
from homo4 import *
np.set_printoptions(precision=4,suppress=True)
H=Rz4(75)@(Rx4(-30)@Rz4(45)@Rx4(-60))
print(H)
