import numpy as np
from fqua import qprod
q1=np.array([0.70711,0.56695,-0.37796,0.18898])
r=np.array([0,5,2,-6])
q2=np.array([0.70711,-0.56695,0.37796,-0.18898])
q3=qprod(q1,r)
q=qprod(q3,q2)
print(q)