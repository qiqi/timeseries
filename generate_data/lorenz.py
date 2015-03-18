from numpy import *
from scipy.integrate import odeint

def lorenz(u, rho):
    sigma, beta = 10, 8./3
    x, y, z = u
    dxdt, dydt, dzdt = sigma*(y-x), x*(rho-z)-y, x*y - beta*z
    return array([dxdt, dydt, dzdt])

u0 = array([2., 10., 10.])
t = linspace(0,1000,10001)
x = odeint(lambda u, t : lorenz(u, 30), u0, t)

savetxt('../data/lorenz.txt', x[:,0])
