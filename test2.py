import matplotlib.pyplot as plt
ax1 = plt.subplot(122)

#在第一个子区域中绘图
plt.scatter([1,3,5],[2,4,5],marker="v",s=50,color="r")
#选中第二个子区域，并绘图
ax2 = plt.subplot(121)
plt.plot([2,4,6],[7,9,15])

#为第一个画板的第一个区域添加标题
ax1.set_title("第一个画板中第一个区域")
ax2.set_title("第一个画板中第二个区域")

# 调整每隔子图之间的距离
plt.tight_layout()
plt.show()

