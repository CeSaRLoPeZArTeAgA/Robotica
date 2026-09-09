import numpy as np
from fquad import h2q
np.set_printoptions(precision=4,suppress=True)
H=np.array([[1,0,0,0],
           [0,1/np.sqrt(2),-1/np.sqrt(2),0],
           [0,1/np.sqrt(2),1/np.sqrt(2),0],
            [0,0,0,1]])
print(h2q(H))