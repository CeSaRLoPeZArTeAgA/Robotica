import numpy as np
def Rx(t): #sexagesimal
    t=np.radians(t)
    c,s=np.cos(t),np.sin(t)
    return np.array([[1, 0,0],
                     [0,c,-s],
                     [0,s,c]])

def Ry(t): #sexagesimal
    t=np.radians(t)
    c,s=np.cos(t),np.sin(t)
    return np.array([[c, 0,s],
                     [0,1,0],
                     [-s,0,c]])

def Rz(t): #sexagesimal
    t=np.radians(t)
    c,s=np.cos(t),np.sin(t)
    return np.array([[c, -s,0],
                     [s,c,0],
                     [0,0,1]])

def Rotpar(k,t,p): #sexagesimal
    t=np.radians(t)
    c,s=np.cos(t),np.sin(t)
    k=k/np.linalg.norm(k)
    return p*c+np.cross(k,p)*s+k*np.dot(k,p)*(1-c)


def Rxh(t):
    t=np.radians(t)
    c,s=np.cos(t),np.sin(t)
    return np.array([[1, 0,0,0],
                     [0,c,-s,0],
                     [0,s,c,0],
                     [0,0,0,1]])
    
def Ryh(t): #sexagesimal
     t=np.radians(t)
     c,s=np.cos(t),np.sin(t)
     return np.array([[c, 0,s,0],
                      [0,1,0,0],
                      [-s,0,c,0],
                      [0,0,0,1]])   
 
def Rzh(t): #sexagesimal
     t=np.radians(t)
     c,s=np.cos(t),np.sin(t)
     return np.array([[c, -s,0,0],
                      [s,c,0,0],
                      [0,0,1,0],
                      [0,0,0,1]])   
 
def Th(x,y,z): #sexagesimal
       return np.array([[1,0,0,x],
                        [0,1,0,y],
                        [0,0,1,z],
                        [0,0,0,1]])  
    
    
    

