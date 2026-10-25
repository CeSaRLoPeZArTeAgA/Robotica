# fqua.py
import numpy as np
def qrotk(k,t):
    k_unit=k/np.linalg.norm(k)
    t=np.radians(t)/2
    s=np.cos(t)
    v=k_unit * np.sin(t)
    return np.insert(v,0,s)

def qprod(q1,q2):
    s1,v1=q1[0],q1[1:]
    s2,v2=q2[0],q2[1:]
    s3=s1*s2-np.dot(v1,v2)
    v3=np.cross(v1,v2)+s1*v2+s2*v1
    return np.insert(v3,0,s3)

def htoq(H):
    nx,ox,ax=H[0,0],H[0,1],H[0,2]
    ny,oy,ay=H[1,0],H[1,1],H[1,2]
    nz,oz,az=H[2,0],H[2,1],H[2,2]
    q0=0.5*np.sqrt(nx+oy+az+1)
    q1=np.sign(oz-ay)*0.5*np.sqrt(nx-oy-az+1)
    q2=np.sign(ax-nz)*0.5*np.sqrt(-nx+oy-az+1)
    q3=np.sign(ny-ox)*0.5*np.sqrt(-nx-oy+az+1)
    return np.array([q0,q1,q2,q3])


