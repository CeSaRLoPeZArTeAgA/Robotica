import numpy as np

# --- Rotaciones homogeneas ---
def Rx4(a):
    a = np.deg2rad(a); c, s = np.cos(a), np.sin(a)
    return np.array([[1, 0, 0, 0],
                     [0, c,-s, 0],
                     [0, s, c, 0],
                     [0, 0, 0, 1]])

def Ry4(a):
    a = np.deg2rad(a); c, s = np.cos(a), np.sin(a)
    return np.array([[ c, 0, s, 0],
                     [ 0, 1, 0, 0],
                     [-s, 0, c, 0],
                     [ 0, 0, 0, 1]])

def Rz4(a):
    a = np.deg2rad(a); c, s = np.cos(a), np.sin(a)
    return np.array([[c,-s, 0, 0],
                     [s, c, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

# --- Traslación homogenea ---
def T4(tx, ty, tz):
    return np.array([[1, 0, 0, tx],
                     [0, 1, 0, ty],
                     [0, 0, 1, tz],
                     [0, 0, 0, 1]])

# Quaternio
def Rot(k,t):
    k=k/np.linalg.norm(k)
    t = np.deg2rad(t)/2
    q0=np.cos(t)
    q1=k[0]*np.sin(t)
    q2=k[1]*np.sin(t)
    q3=k[2]*np.sin(t)
    return np.array([q0,q1,q2,q3])
    
