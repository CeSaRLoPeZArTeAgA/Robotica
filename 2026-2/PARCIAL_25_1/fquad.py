import numpy as np

# Quaternio
def Rot(k,t):
    k=k/np.linalg.norm(k)
    t = np.deg2rad(t)/2
    q0=np.cos(t)
    q1=k[0]*np.sin(t)
    q2=k[1]*np.sin(t)
    q3=k[2]*np.sin(t)
    return np.array([q0,q1,q2,q3])

#Rotacion a cuaternio
def h2q(H):
    nx,ox,ax=H[0,0],H[0,1],H[0,2]
    ny,oy,ay=H[1,0],H[1,1],H[1,2]
    nz,oz,az=H[2,0],H[2,1],H[2,2]
    q0=1/2*np.sqrt(nx+oy+az+1)
    q1=np.sign(oz-ay)*1/2*np.sqrt(nx-oy-az+1)
    q2=np.sign(ax-nz)*1/2*np.sqrt(-nx+oy-az+1)
    q3=np.sign(ny-ox)*1/2*np.sqrt(-nx-oy+az+1)
    return np.array([q0,q1,q2,q3])

#Producto de cuaternios Q3 = Q1 * Q2
def qprod(q1,q2):
    s1,v1=q1[0],q1[1:]
    s2,v2=q2[0],q2[1:]
    s3=s1*s2-np.dot(v1,v2)
    v3=np.cross(v1,v2)+s1*v2+s2*v1
    return np.insert(v3,0,s3)

#Cuaternio a matriz homogenea
def q2h(q):
    q0,q1,q2,q3=q[0],q[1],q[2],q[3]
    H=2*np.array([[q0*q0+q1*q1-1/2,q1*q2-q3*q0,q1*q3+q2*q0,0],
               [q1*q2+q3*q0,q0*q0+q2*q2-1/2,q2*q3-q1*q0,0],
               [q1*q3-q2*q0,q2*q3+q1*q0,q0*q0+q3*q3-1/2,0],
                [0,0,0,1/2]])
    return(H)

#Conjugado de cuaternio
def qconj(q):
    q[1:]=-q[1:]
    return q







