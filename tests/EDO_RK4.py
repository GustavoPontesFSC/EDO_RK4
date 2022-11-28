#!/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
p = os.path.abspath('.')
sys.path.insert(1,p)

import numpy as np
import matplotlib.pyplot as plt
from math_func.fuctions import population
from math_func.operation import RK4

t0 = 0
tf = 30
h = 0.005
x0 = y0 = 2

alfa = 1
beta = 0.5
gama = 0.5
delta = 2

C = (alfa,beta,gama,delta)
N = int((tf-t0)/h)

r,t = RK4((x0,y0), t0,tf, f=population, h=h, C=C)

x = r[:,0]
y = r[:,1]
plt.plot(t,x)
plt.plot(t,y)
plt.show()