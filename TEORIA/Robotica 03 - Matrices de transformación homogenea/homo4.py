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

