import sympy as sp
a, tx, ty, tz = sp.symbols("a tx ty tz")
# --- Rotaciones homogéneas ---
# ángulo a en grados sexagesimales
# Rotación homogénea alrededor del eje X
def Rxhs(a):
    a = sp.rad(a)   # convierte grados a radianes simbólicamente
    c, s = sp.cos(a), sp.sin(a)
    return sp.Matrix([
        [1, 0,  0, 0],
        [0, c, -s, 0],
        [0, s,  c, 0],
        [0, 0,  0, 1]
    ])

def Ryhs(a):
    a = sp.rad(a);
    c, s = sp.cos(a), sp.sin(a)
    return sp.Matrix([[ c, 0, s, 0],
                     [ 0, 1, 0, 0],
                     [-s, 0, c, 0],
                     [ 0, 0, 0, 1]])

def Rzhs(a):
    a = sp.rad(a) 
    c, s = sp.cos(a), sp.sin(a)
    return sp.Matrix([[c,-s, 0, 0],
                     [s, c, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

# --- Traslación homogenea ---
def Ths(tx, ty, tz):
    return sp.Matrix([[1, 0, 0, tx],
                     [0, 1, 0, ty],
                     [0, 0, 1, tz],
                     [0, 0, 0, 1]])

