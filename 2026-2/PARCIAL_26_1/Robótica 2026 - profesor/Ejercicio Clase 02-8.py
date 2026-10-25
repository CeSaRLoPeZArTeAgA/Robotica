import numpy as np
from rot3D import Rotpar
k=np.array([1,1,0])
t=45
p=np.array([2,1,0])
v=Rotpar(k,t,p)
print(v)