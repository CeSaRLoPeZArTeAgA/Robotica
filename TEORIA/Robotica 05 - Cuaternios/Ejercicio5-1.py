import numpy as np
from homo4 import *
np.set_printoptions(precision=4,suppress=True)
k=np.array([3,-2,1])
t=90
Q=Rot(k,t)
print(Q)

