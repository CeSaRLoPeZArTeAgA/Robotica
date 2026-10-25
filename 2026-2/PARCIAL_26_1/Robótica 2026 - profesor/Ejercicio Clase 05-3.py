import numpy as np
from fqua import htoq
H=np.array([[1,0,0,0],
             [0,1/np.sqrt(2),-1/np.sqrt(2),0],
             [0,1/np.sqrt(2),1/np.sqrt(2),0]
             ])
Q=htoq(H)
print(Q)