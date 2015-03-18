from pylab import *
from numpy import *

INPUT_DATA = ['./data/sin.txt', './data/sin_plus_exp.txt',
              './data/vanderpol.txt', './data/lorenz.txt']

for INPUT in INPUT_DATA:
    xAll = loadtxt(INPUT)
    n_series = arange(200, xAll.size, 50)
    mean_series, mean_series_3_stage = [], []
    for n in n_series:
        x = xAll[:n]
        mean_series.append(x.mean())
    
        A = transpose([ones(x.size - 2), x[:-2], x[1:-1]])
        b = x[2:]
        a, residuals, rank, s = linalg.lstsq(A, b)
        mean_series_3_stage.append(a[0])
    
    figure()
    subplot(2,1,1)
    plot(xAll)
    subplot(2,1,2)
    plot(n_series, abs(array(mean_series)), 'o')
    plot(n_series, abs(array(mean_series_3_stage)), 'd')
    grid()
