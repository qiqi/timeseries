from numpy import *
t = linspace(0,100,1001)
x = sin(t) + exp(-t * 0.1)
savetxt('../data/sin_plus_exp.txt', x)
