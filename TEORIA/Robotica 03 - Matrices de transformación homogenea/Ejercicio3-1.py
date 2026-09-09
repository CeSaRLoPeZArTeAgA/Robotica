import numpy as np
from homo4 import T4,Rz4
np.set_printoptions(precision=4,suppress=True)

# Construimos H = T @ Rz
H = T4(2,3,0) @ Rz4(45)
print("H = \n",H)