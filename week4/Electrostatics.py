def import numpy as np

def pointPotential(x,y,q,posx,posy):
    """in meters and nC"""
    k = 8.9875518*10**9 #setting k, q, and d values
    Vyx = (k*q)/(x**2 + y**2)**(1/2.) #insert Vxy function
    return Vyx

def dipolePotential(x,y,q,d):
    """in m and nC"""
    k = 8.9875518*10**9 #setting k, q, and d values
    Vxy = (k*q/((x)**2 + (y - d)**2)**(1/2.) - (k*q/(x**2 + (y + d)**2)**(1/2.))) #insert Vxy function
    return Vxy #return Vxy

def pointField(x,y,q,Xq,Yq):
    """finds Ex and Ey of an electric field of charge q and positions (Xq,Yq)"""
    Ex = ((k*q)(x-Xq))/((x-Xq)**2 + (y-Yq)**2)**(.5)
    Ey = ((k*q)(y-Yq))/((x-Xq)**2 + (y-Yq)**2)**(.5)
