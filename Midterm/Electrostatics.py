import numpy as np


def pointField(x,y,q,Xq,Yq):
    """finds Ex and Ey of an electric field of charge q and positions (Xq,Yq)"""
    k = 8.9875518*10**9
    Ex = ((k*q)(x-Xq))/((x-Xq)**2 + (y-Yq)**2)**(.5)
    Ey = ((k*q)(y-Yq))/((x-Xq)**2 + (y-Yq)**2)**(.5)
    return Ex, Ey
