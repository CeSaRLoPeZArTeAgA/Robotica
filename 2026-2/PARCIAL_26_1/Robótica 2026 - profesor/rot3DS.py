import sympy as sp
t, x, y, z = sp.symbols("t x y z")
def Rxs(t): #sexagesimal
    t=sp.rad(t)
    c,s=sp.cos(t),sp.sin(t)
    return sp.Matrix([[1, 0,0],
                     [0,c,-s],
                     [0,s,c]])

def Rys(t): #sexagesimal
    t=sp.rad(t)
    c,s=sp.cos(t),sp.sin(t)
    return sp.Matrix([[c, 0,s],
                     [0,1,0],
                     [-s,0,c]])

def Rzs(t): #sexagesimal
    t=sp.rad(t)
    c,s=sp.cos(t),sp.sin(t)
    return sp.Matrix([[c, -s,0],
                     [s,c,0],
                     [0,0,1]])

def Rotpars(k,t,p): #sexagesimal
    t=sp.rad(t)
    c,s=sp.cos(t),sp.sin(t)
    k=k/sp.linalg.norm(k)
    return p*c+sp.cross(k,p)*s+k*sp.dot(k,p)*(1-c)


def Rxhs(t):
    t=sp.rad(t)
    c,s=sp.cos(t),sp.sin(t)
    return sp.Matrix([[1, 0,0,0],
                     [0,c,-s,0],
                     [0,s,c,0],
                     [0,0,0,1]])
    
def Ryhs(t): #sexagesimal
     t=sp.rad(t)
     c,s=sp.cos(t),sp.sin(t)
     return sp.Matrix([[c, 0,s,0],
                      [0,1,0,0],
                      [-s,0,c,0],
                      [0,0,0,1]])   
 
def Rzhs(t): #sexagesimal
     t=sp.rad(t)
     c,s=sp.cos(t),sp.sin(t)
     return sp.Matrix([[c, -s,0,0],
                      [s,c,0,0],
                      [0,0,1,0],
                      [0,0,0,1]])   
 
def Ths(x,y,z): #sexagesimal
       return sp.Matrix([[1,0,0,x],
                        [0,1,0,y],
                        [0,0,1,z],
                        [0,0,0,1]])  
    
    
    
    

