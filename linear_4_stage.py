from pylab import *
from numpy import *

INPUT_DATA = ['./data/sin.txt', './data/sin_plus_exp.txt',
              './data/vanderpol.txt', './data/lorenz.txt',
              './data/pressure.txt']
# INPUT_DATA = ['./data/vanderpol.txt']

for INPUT in INPUT_DATA:
    xAll = loadtxt(INPUT)
    n_series = arange(200, xAll.size, 50)
    mean_series, mean_series_4_stage = [], []
    for n in n_series:
        x = xAll[:n]
        mean_series.append(x.mean())
    
        A = transpose([ones(x.size - 4), x[:-4], x[2:-2], x[3:-1]])
        b = x[4:]
        ridge = (x**2).sum() * 0.1
        a = linalg.solve(dot(A.T, A) + ridge * eye(4), dot(A.T, b))
        mean_series_4_stage.append(a[0] / (1 - a[1:].sum()))
    
    print(a)
    figure()
    subplot(2,1,1)
    plot(xAll)
    subplot(2,1,2)
    plot(n_series, abs(array(mean_series)), 'o')
    plot(n_series, abs(array(mean_series_4_stage)), ':d')
    grid()
