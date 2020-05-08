# 模拟数据获取
from airplane import Airplane
from receiver import Receiver
import matplotlib.pyplot as plt
import numpy as np
from math import radians, cos, sin, asin, sqrt, pi, atan

airplane1 = Airplane('782034',[120.128234,30.2141348,10000],[115.86143245,28.750012,10000],180,3340)
receiver1 = Receiver([114.122588,36.548925,1000])
time_track1 =receiver1.fin_time_track(airplane1)
track1 = airplane1.track

# 预处理step1
# 获取前后数据包时间差


using_data = time_track1
time_error = []
location_error = []
print(len(track1), len(using_data))

for i in range(len(using_data) - 1):
    time_error.append(using_data[i + 1] - using_data[
        i] - 50000000)  # -(airplane1.geodistance(track1[i+1],receiver1.location)-airplane1.geodistance(track1[i],receiver1.location))*10/3)
    location_error.append(
        (airplane1.geodistance(track1[i + 1], receiver1.location) - airplane1.geodistance(track1[i], receiver1.location))*10/3 + 600)

# plt.plot(using_data[19:79], test_data[19:79])
# plt.plot(using_data[:-1], time_error)
# plt.show()
# plt.ylim(0.39,0.6)
# plt.xlim(0.39,0.6)
# plt.plot(using_data[:-1], location_error)
# plt.show()

# 初试的估计导弹的位置就直接用GPS测量的位置
predicts = [time_error[0]]
position_predict = predicts[0]

predict_var = 0
odo_var = 50 ** 2  # 这是我们自己设定的位置测量仪器的方差，越大则测量值占比越低
v_std = 10  # 测量仪器的方差
for i in range(1, len(using_data[:-1])):
    dv = (time_error[i] - time_error[i - 1]) + np.random.normal(0, 50)  # 模拟从IMU读取出的速度
    position_predict = position_predict + dv  # 利用上个时刻的位置和速度预测当前位置
    predict_var += v_std ** 2  # 更新预测数据的方差
    # 下面是Kalman滤波
    position_predict = position_predict * odo_var / (predict_var + odo_var) + time_error[i] * predict_var / (
                predict_var + odo_var)
    predict_var = (predict_var * odo_var) / (predict_var + odo_var) ** 2
    predicts.append(position_predict)
plt.plot(using_data[:-1], time_error)

plt.plot(using_data[:-1], predicts, label='kalman filtered position')
plt.plot(using_data[:-1], location_error)
plt.legend()
plt.show()
