function [ slope,intercept,slerr,interr ] = weightedLSQFit( x,y,w )
% Take in arrays representing (x,y) values for a set of linearly varying
% data and an array of weights w.  Preform a weighted linear least squares 
% regression. Return the resulting slope and intercept parameters of the 
% best fit line with their uncertainties.
wsum = sum(w);
w_x = sum(w.*x); 
w_x2 = sum(w.*(x.^2));
w_y = sum(w.*y);
w_xy = sum(w.*x.*y); 
slope = (wsum.*w_xy - w_x.*w_y)/(wsum.*w_x2 - w_x.^2);
intercept = (w_x2.*w_y - w_x.*w_xy)/(wsum.*w_x2 - w_x.^2);
slerr = (wsum/((wsum.*w_x2) - (w_x.^2))).^(.5);
interr = (w_x2/(wsum.*w_x2 - w_x.^2)).^(.5);
end