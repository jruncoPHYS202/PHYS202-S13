def pointField(x,y,q,Xq,Yq):
    """finds Ex and Ey of an electric field of charge q and positions (Xq,Yq)"""
    Ex = ((k*q)(x-Xq))/((x-Xq)**2 + (y-Yq)**2)**(.5)
    Ey = ((k*q)(y-Yq))/((x-Xq)**2 + (y-Yq)**2)**(.5)

