import numpy as np
import matplotlib.pyplot as plt

# 模拟数据
t = np.linspace(1, 100, 100)
a = 0.5
position = (a * t * 2) / 2

position_noise = position + np.random.normal(0, 1200, size=(t.shape[0]))

plt.plot(t, position, label='truth position')
plt.plot(t, position_noise, label='only use measured position')

# 初试的估计导弹的位置就直接用GPS测量的位置
predicts = [position_noise[0]]
position_predict = predicts[0]

predict_var = 0
odo_var = 200 ** 2  # 这是我们自己设定的位置测量仪器的方差，越大则测量值占比越低
v_std = 50  # 测量仪器的方差
for i in range(1, t.shape[0]):
    dv = (position[i] - position[i - 1]) + np.random.normal(0, 50)  # 模拟从IMU读取出的速度
    position_predict = position_predict + dv  # 利用上个时刻的位置和速度预测当前位置
    predict_var += v_std ** 2  # 更新预测数据的方差
    # 下面是Kalman滤波
    position_predict = position_predict * odo_var / (predict_var + odo_var) + position_noise[i] * predict_var / (
                predict_var + odo_var)
    predict_var = (predict_var * odo_var) / (predict_var + odo_var) ** 2
    predicts.append(position_predict)

plt.plot(t, predicts, label='kalman filtered position')

plt.legend()
plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# # 创建一个0-99的一维矩阵
# z = [i for i in range(100)]
# z_watch = np.mat(z)
#
#
# # 创建一个方差为1的高斯噪声，精确到小数点后两位
# noise = np.round(np.random.normal(0, 1, 100), 2)
# noise_mat = np.mat(noise)
# # 将z的观测值和噪声相加
# z_mat = z_watch + noise_mat
# print(z_watch)
# print(z_mat)
#
# # 定义x的初始状态
# x_mat = np.mat([[0, ], [0, ]])
# # 定义初始状态协方差矩阵
# p_mat = np.mat([[1, 0], [0, 1]])
# # 定义状态转移矩阵，因为每秒钟采一次样，所以delta_t = 1
# f_mat = np.mat([[1, 1], [0, 1]])
# # 定义状态转移协方差矩阵，这里我们把协方差设置的很小，因为觉得状态转移矩阵准确度高
# q_mat = np.mat([[0.0001, 0], [0, 0.0001]])
# # 定义观测矩阵
# h_mat = np.mat([1, 0])
# # 定义观测噪声协方差
# r_mat = np.mat([1])
# for i in range(100):
#     x_predict = f_mat * x_mat
#     p_predict = f_mat * p_mat * f_mat.T + q_mat
#     kalman = p_predict * h_mat.T / (h_mat * p_predict * h_mat.T + r_mat)
#     x_mat = x_predict + kalman * (z_mat[0, i] - h_mat * x_predict)
#     p_mat = (np.eye(2) - kalman * h_mat) * p_predict
#     plt.plot(x_mat[0, 0], x_mat[1, 0], 'ro', markersize=1)
# plt.show()


# # 小波变换
# import sys
#
# import matplotlib.pyplot as plt
# import numpy as np
# import pywt
#
# try:
#     wavelet = pywt.Wavelet('sym5')
#     try:
#         level =5# int(sys.argv[2])
#     except IndexError as e:
#         level = 10
# except ValueError as e:
#     print("Unknown wavelet")
#     raise SystemExit
# except IndexError as e:
#     raise SystemExit
#
#
# data = wavelet.wavefun(level)
# if len(data) == 2:
#     x = data[1]
#     psi = data[0]
#     fig = plt.figure()
#     if wavelet.complex_cwt:
#         plt.subplot(211)
#         plt.title(wavelet.name+' real part')
#         mi, ma = np.real(psi).min(), np.real(psi).max()
#         margin = (ma - mi) * 0.05
#         plt.plot(x,np.real(psi))
#         plt.ylim(mi - margin, ma + margin)
#         plt.xlim(x[0], x[-1])
#         plt.subplot(212)
#         plt.title(wavelet.name+' imag part')
#         mi, ma = np.imag(psi).min(), np.imag(psi).max()
#         margin = (ma - mi) * 0.05
#         plt.plot(x,np.imag(psi))
#         plt.ylim(mi - margin, ma + margin)
#         plt.xlim(x[0], x[-1])
#     else:
#         mi, ma = psi.min(), psi.max()
#         margin = (ma - mi) * 0.05
#         plt.plot(x,psi)
#         plt.title(wavelet.name)
#         plt.ylim(mi - margin, ma + margin)
#         plt.xlim(x[0], x[-1])
# else:
#     funcs, x = data[:-1], data[-1]
#     labels = ["scaling function (phi)", "wavelet function (psi)",
#               "r. scaling function (phi)", "r. wavelet function (psi)"]
#     colors = ("r", "g", "r", "g")
#     fig = plt.figure()
#     for i, (d, label, color) in enumerate(zip(funcs, labels, colors)):
#         mi, ma = d.min(), d.max()
#         margin = (ma - mi) * 0.05
#         ax = fig.add_subplot((len(data) - 1) // 2, 2, 1 + i)
#
#         ax.plot(x, d, color)
#         ax.set_title(label)
#         ax.set_ylim(mi - margin, ma + margin)
#         ax.set_xlim(x[0], x[-1])
#
# plt.show()
#
