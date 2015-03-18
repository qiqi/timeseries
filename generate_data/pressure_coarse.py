from numpy import *
p = loadtxt('../data/pressure.txt')
savetxt('../data/pressure_coarse.txt', p[::10])
