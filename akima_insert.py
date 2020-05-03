# akima插值法的实现
import numpy as np
from scipy.interpolate import  UnivariateSpline, Akima1DInterpolator, PchipInterpolator
import matplotlib.pyplot as plt

x_data = np.array([1.2371, 1.6809, 2.89151])

y_data = np.array([ 0.0490012, 0.0332843, 0.0235889])

x_data_smooth = np.linspace(min(x_data), max(x_data), 100)
fig, ax = plt.subplots(1,1)

# spl = UnivariateSpline(x_data, y_data, s=0, k=2)
# y_data_smooth = spl(x_data_smooth)
# ax.plot(x_data_smooth, y_data_smooth, 'b')

bi = Akima1DInterpolator(x_data, y_data)

y_data_smooth = bi(x_data_smooth)
ax.plot(x_data_smooth, y_data_smooth, 'r.')

# bi = PchipInterpolator(x_data, y_data)
# y_data_smooth = bi(x_data_smooth)
# ax.plot(x_data_smooth, y_data_smooth, 'r')

ax.scatter(x_data, y_data)

plt.show()