import numpy as np
np.set_printoptions(precision=4,suppress=True)
R12=np.array([[1,0,0,0],
             [0,1/2,-np.sqrt(3)/2,0],
             [0,np.sqrt(3)/2,1/2,0],
             [0,0,0,1]
             ])
R13=np.array([[0,0,-1,0],
             [0,1,0,0],
             [1,0,0,0],
             [0,0,0,1]
             ])
# R23=R21@R13
R23=np.linalg.inv(R12)@R13
print(R23)
