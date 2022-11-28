import numpy as np

def RK4(r0, t0, tf, f, N='', h='', C=''):
    if h == '' and N == '':
        ValueError('N or h need recive a value!')
    elif type(N) == int and (type(h)== int or type(h)==float):
        ValueError('Only one of the two should receive a value!')
    if type(N) == int:
        h = (tf-t0)/N
    elif type(h) == float or type(h) == int:
        N = int((tf-t0)/h)
    M = len(r0)
    r = np.zeros((N,M))
    t = np.zeros(N)

    r[0] = r0
    t[0] = t0

    for i in range(N):
        t[i] = t0 + h*(i)
    for j in range(N-1):
        k1 = h*f(r[j,:] , t[j], *C)
        k2 = h*f(r[j,:] + k1/2 , t[j] + h/2, *C)
        k3 = h*f(r[j,:] + k2/2 , t[j] + h/2, *C)
        k4 = h*f(r[j,:] + k3 , t[j] + h, *C)
        r[j + 1] = r[j,:] + 1/6*(k1+2*k2+2*k3+k4) 
    return (r,t)