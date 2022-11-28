import numpy as np

def population(r,t, alfa, beta, gama, delta):
    x = r[0]
    y = r[1]
    x_ = alfa*x-beta*x*y
    y_ =gama*x*y - delta*y

    return np.array([x_,y_])