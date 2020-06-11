import numpy as np
import random
import matplotlib.pyplot as plt



def plttt(a,c):
    b = np.sqrt(c * c - a * a)
    x3 = np.arange(a, 100, 0.1)
    y3 = b / a * np.sqrt(x3 * x3 - a * a)
    x4 = np.arange(a, 100, 0.1)
    y4 = -b / a * np.sqrt(x4 * x4 - a * a)

    return x3, y3, x4, y4

ax1 = plt.subplot(331)
c = 0.5
plt.plot([-c,c],[0,0],'b.')
x3, y3, x4, y4 = plttt(0.005,c)
plt.plot(x3, y3,'r', x4, y4,'r')
x3, y3, x4, y4 = plttt(0.155,c)
plt.plot(x3, y3,'r', x4, y4,'r')
plt.ylim(-100,100)
plt.xlim(-100,100)
plt.ylabel("阈值范围为0.3，中值为0.15")

ax2 = plt.subplot(332)
c = 1
plt.plot([-c,c],[0,0],'b.')
x3, y3, x4, y4 = plttt(0.005,c)
plt.plot(x3, y3,'r', x4, y4,'r')
x3, y3, x4, y4 = plttt(0.155,c)
plt.plot(x3, y3,'r', x4, y4,'r')
plt.ylim(-100,100)
plt.xlim(-100,100)

ax3 = plt.subplot(333)
c = 10
plt.plot([-c,c],[0,0],'b.')
x3, y3, x4, y4 = plttt(0.005,c)
plt.plot(x3, y3,'r', x4, y4,'r')
x3, y3, x4, y4 = plttt(0.155,c)
plt.plot(x3, y3,'r', x4, y4,'r')
plt.ylim(-100,100)
plt.xlim(-100,100)

ax4 = plt.subplot(334)
c = 0.5
plt.plot([-c,c],[0,0],'b.')
x3, y3, x4, y4 = plttt(0.075,c)
plt.plot(x3, y3,'r', x4, y4,'r')
x3, y3, x4, y4 = plttt(0.225,c)
plt.plot(x3, y3,'r', x4, y4,'r')
plt.ylim(-100,100)
plt.xlim(-100,100)
plt.ylabel("阈值范围为0.3，中值为0.3")


ax5 = plt.subplot(335)
c = 1
plt.plot([-c,c],[0,0],'b.')
x3, y3, x4, y4 = plttt(0.075,c)
plt.plot(x3, y3,'r', x4, y4,'r')
x3, y3, x4, y4 = plttt(0.225,c)
plt.plot(x3, y3,'r', x4, y4,'r')
plt.ylim(-100,100)
plt.xlim(-100,100)

ax6 = plt.subplot(336)
c = 10
plt.plot([-c,c],[0,0],'b.')
x3, y3, x4, y4 = plttt(0.075,c)
plt.plot(x3, y3,'r', x4, y4,'r')
x3, y3, x4, y4 = plttt(0.225,c)
plt.plot(x3, y3,'r', x4, y4,'r')
plt.ylim(-100,100)
plt.xlim(-100,100)

ax7 = plt.subplot(337)
c = 0.5
plt.plot([-c,c],[0,0],'b.')
x3, y3, x4, y4 = plttt(0.005,c)
plt.plot(x3, y3,'r', x4, y4,'r')
x3, y3, x4, y4 = plttt(0.305,c)
plt.plot(x3, y3,'r', x4, y4,'r')
plt.ylim(-100,100)
plt.xlim(-100,100)
plt.ylabel("阈值范围为0.6，中值为0.3")


ax8 = plt.subplot(338)
c = 1
plt.plot([-c,c],[0,0],'b.')
x3, y3, x4, y4 = plttt(0.005,c)
plt.plot(x3, y3,'r', x4, y4,'r')
x3, y3, x4, y4 = plttt(0.305,c)
plt.plot(x3, y3,'r', x4, y4,'r')
plt.ylim(-100,100)
plt.xlim(-100,100)

ax9 = plt.subplot(339)
c = 10
plt.plot([-c,c],[0,0],'b.')
x3, y3, x4, y4 = plttt(0.005,c)
plt.plot(x3, y3,'r', x4, y4,'r')
x3, y3, x4, y4 = plttt(0.305,c)
plt.plot(x3, y3,'r', x4, y4,'r')
plt.ylim(-100,100)
plt.xlim(-100,100)

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
ax1.set_title("焦距为1")
ax2.set_title("焦距为2")
ax3.set_title("焦距为20")

# 调整每隔子图之间的距离
# plt.tight_layout()
plt.show()