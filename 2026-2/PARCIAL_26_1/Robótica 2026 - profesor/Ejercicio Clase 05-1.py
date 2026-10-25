import numpy as np
from fqua import qrotk
u=np.array([3,-2,1])
theta=90
resp= qrotk(u,90)
print (resp)
