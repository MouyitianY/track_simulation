# from random import gauss
# from random import seed
# from pandas import Series
# from pandas.plotting import autocorrelation_plot
# from matplotlib import pyplot
# # seed random number generator
# seed(1)
# # create white noise series
# series= [gauss(0.0,1.0)for i in range(1000)]
# series= Series(series)
# # summary stats
# print(series.describe())
# # line plot
# series.plot()
# pyplot.show()
# # histogram plot
# series.hist()
# pyplot.show()
# # autocorrelation
# autocorrelation_plot(series)
# pyplot.show()


import numpy as np

import matplotlib.pyplot as plt

# 在直线附近生成随机的点


X = np.arange(0, 5, 0.1)

Z = [3 + 5 * x for x in X]

Y = [np.random.normal(z, 0.5) for z in Z]

plt.plot(X, Y, 'ro')

plt.show()


def linear_regression(x, y):
    N = len(x)

    sumx = sum(x)

    sumy = sum(y)

    sumx2 = sum(x ** 2)

    sumxy = sum(x * y)

    A = np.mat([[N, sumx], [sumx, sumx2]])

    b = np.array([sumy, sumxy])

    return np.linalg.solve(A, b)


a0, a1 = linear_regression(X, Y)

print(a0, a1)



#绘制直线

_x = [0,5]

_y = [a0+a1*x for x in _x]

plt.plot(X,Y,'ro',_x,_y,'b',linewidth=2)

plt.title("y={}+{}x".format(a0,a1))

plt.show()
