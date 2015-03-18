from numpy import *
t = linspace(0,100,1001)
x = sin(t)
savetxt('../data/sin.txt', x)
