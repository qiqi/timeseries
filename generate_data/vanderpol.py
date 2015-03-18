from numpy import *
from scipy.integrate import odeint

def vanderpol(u, mu):
    return array([u[1], -u[0] + mu * (1 - u[0]**2) * u[1]])

u0 = array([2., 10.])
t = linspace(0,100,1001)
x = odeint(lambda u, t : vanderpol(u, 1), u0, t)

savetxt('../data/vanderpol.txt', x[:,0])
