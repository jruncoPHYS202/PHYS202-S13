import numpy as np
def LinearLeastSquaresFit(x,y):
    import numpy as np
    """Take in arrays representing (x,y) values for a set of linearly 
    varying data and preform a linear least squares regression.  
    Return the resulting slope and intercept parameters of the best 
    fit line with their uncertainties."""
    averageX = np.sum(x)/len(x) #x average
    averageX2 = np.sum(x**2)/len(x**2) #x^2 average
    averageY = np.sum(y)/len(y) #y average
    averageXY = np.sum(x*y)/len(x*y) #x*y average
    slope = (averageXY-(averageX*averageY))/(averageX2-(averageX**2)) #slope formula
    intercept = (averageX2*averageY - (averageX*averageXY))/(averageX2-(averageX**2)) #intercept formula
    deviation = y - (slope*x + intercept) #deviation to get deviation^2
    deviation2 = np.sum(deviation**2)/len(x) #deviation^2 formula
    slerr = np.sqrt((1/(len(x)-2.))*(deviation2/(averageX2 - (averageX**2)))) #slope uncertainty
    interr = np.sqrt((1/(len(x)-2.))*((deviation2*averageX2)/(averageX2 - (averageX**2)))) #intercept uncertainty
    return slope,intercept,slerr,interr


def WeightedLinearLeastSquaresFit(x,y,w):
    import numpy as np
    """Take in arrays representing (x,y) values for a set of linearly varying data
    and an array of weights w.  Preform a weighted linear least squares regression.
    Return the resulting slope and intercept parameters of the best fit line with 
    their uncertainties."""
    wsum = np.sum(w) 
    w_x = np.sum(w*x) #weighted x sum
    w_x2 = np.sum(w*(x**2)) #weighted x^2 sum
    w_y = np.sum(w*y) #weighted y sum
    w_xy = np.sum(w*x*y) #weighted x*y sum
    slope = (wsum*w_xy - w_x*w_y)/(wsum*w_x2 - w_x**2) #slope formula
    intercept = (w_x2*w_y - w_x*w_xy)/(wsum*w_x2 - w_x**2) #intercept
    if sum(w)/len(w) == 1:
        averageX = np.sum(x)/len(x) #all code for if part is from question 2
        averageX2 = np.sum(x**2)/len(x**2)
        averageY = np.sum(y)/len(y)
        averageXY = np.sum(x*y)/len(x*y)
        deviation = y - (slope*x + intercept) 
        deviation2 = np.sum(deviation**2)/len(x) 
        slerr = np.sqrt((1/(len(x)-2.))*(deviation2/(averageX2 - (averageX**2))))
        interr = np.sqrt((1/(len(x)-2.))*((deviation2*averageX2)/(averageX2 - (averageX**2))))
    else:
        slerr = np.sqrt(wsum/((wsum*w_x2) - (w_x**2))) #weighted slope error
        interr = np.sqrt(w_x2/(wsum*w_x2 - w_x**2)) #weighted intercept error
    return slope,slerr,intercept,interr
