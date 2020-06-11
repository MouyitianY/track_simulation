from airplane import Airplane
from attacker import Attacker
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

class Receiver():
    def __init__(self, location, dirfting = 500, NoiseRange = (-200,200)):
        '''
        :param location: [lng,lat,high] 接收器坐标
        '''
        self.location = location
        # 飞机字典
        self.airplane_dic = {}
        # 幽灵飞机字典
        self.ghost_dic = {}
        self.dirfting = dirfting
        self.NoiseRange = NoiseRange

    # 噪声
    def nosie(self):
        # 高斯白噪声
        return random.uniform(self.NoiseRange[0], self.NoiseRange[1])

    # 飞机与地面接收器的时钟漂移
    def drift(self, time_gap):
        '''
        :param dirfting: 每1秒钟漂移的纳秒数(与基准时间相比)
        :return:
        '''
        drift = self.dirfting * time_gap
        return drift

    # 获取最终的接收时间轨迹
    def fin_time_track(self,airplane):
        '''
        :param airplane: Airplane
        :return:
        '''
        # 初始化到达时间序列
        time_track=[]
        track = airplane.track
        msg_num = len(track)
        # print(msg_num)

        # 时间间隔：用来计算时钟漂移（drift = self.dirfting * time_gap）
        time_gap = [0]
        for i in range(msg_num-1):
            # print(i)
            time_gap.append(airplane.send_time_set[i+1]-airplane.send_time_set[0])

        for i in range(msg_num):
            # 飞行时间（TOF） = 漂移+噪音+信号飞行时间(包含时钟不同步与误差)
            time_of_flight = self.drift(time_gap[i]) + self.nosie() + \
                             airplane.geodistance(track[i],self.location)*10/3
            time_of_flight = time_of_flight/1000000000

            # 每一个到达时间 = 发送时间 + TOF
            time_track.append(airplane.send_time_set[i] + time_of_flight)

        self.airplane_dic[airplane.icao] = tuple(time_track)
        airplane.time_track = time_track
        return time_track


    def ghost_time_track(self, ghost):
        '''
        :param ghost:
        :return:time_track
        '''
        # 初始化到达时间序列
        time_track = []
        track = ghost.track
        msg_num = len(track)

        # 时间间隔：用来计算时钟漂移（drift = self.dirfting * time_gap）
        time_gap = [0]
        for i in range(msg_num - 1):
            # print(i)
            time_gap.append(ghost.send_time_set[i + 1] - ghost.send_time_set[0])

        for i in range(msg_num):
            # 飞行时间（TOF） = 漂移+噪音+信号飞行时间(包含时钟不同步与误差)
            time_of_flight = self.drift(time_gap[i]) + self.nosie() + \
                             ghost.geodistance(ghost.ghost_flag, self.location) * 10 / 3
            time_of_flight = time_of_flight / 1000000000

            # 每一个到达时间 = 发送时间 + TOF
            time_track.append(ghost.send_time_set[i] + time_of_flight)


        self.ghost_dic[ghost.icao] = tuple(time_track)
        ghost.time_track = time_track
        return time_track




    # 绘制接收器与飞机轨迹坐标图
    def plt_location(self,airplane):
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        track = airplane.track
        lng = []
        lat = []
        high = []
        for position in track:
            lng.append(position[0])
            lat.append(position[1])
            high.append(position[2])
        ax.plot(lng, lat, high, 'b.')
        ax.scatter(self.location[0], self.location[1], self.location[2], 'r.')
        ax.legend()
        plt.show()


# receiver = Receiver([118,29,1000],dirfting=500)
# receiver2 = Receiver([118,29,1000],dirfting=500)
# attacker = Attacker([116,30,1000],1)
# ghost_time_track1 = receiver.ghost_time_track(attacker.ghost_list[0])
# ghost_time_track2 = receiver2.ghost_time_track(attacker.ghost_list[0])
# print(ghost_time_track1)
# print(ghost_time_track2)
# tdoa= []
# for i in range(len(ghost_time_track1)):
#     tdoa.append(ghost_time_track1[i]-ghost_time_track2[i])
# plt.plot(tdoa)
# plt.show()
# airplane = Airplane('782034', [120, 30, 8500], [115, 28, 7500], 180, 0)#1564503340



# receiver.plt_location(airplane)
# print(receiver.fin_time_track(airplane))
# print(receiver2.fin_time_track(airplane))
# print(receiver.airplane_dic["782034"])
# print(receiver2.airplane_dic["782034"])
# receiver.plt_location(airplane)

# time_track =receiver.fin_time_track(airplane)
# time_track2 = receiver.ghost_time_track(attacker.ghost_list[0])
# # print(track)+
# plt.plot(track2)
# plt.show()
# receiver.plt_location(airplane)



# 测试前后数据包的时间差
# time_error = []
# track = airplane.track
#
# for i in range(len(time_track)-1):
#     time_error.append(time_track[i+1]-time_track[i]-0.5*100000000
#                       - (airplane.geodistance(track[i+1],receiver.location) - airplane.geodistance(track[i],receiver.location))*10/3)
#     # print(track[i+1]-track[i]-0.5*100000000)
#     # print(airplane.geodistance(point[i+1],receiver.location) - airplane.geodistance(point[i],receiver.location))
# plt.plot(time_error,'.')
# plt.show()

# time_error = []
# track2 = attacker.ghost_list[0].track
# for i in range(len(time_track2) - 1):
#     time_error.append(time_track2[i + 1] - time_track2[i] - 0.5 * 100000000 - (
#                 airplane.geodistance(track2[i + 1], receiver.location) - airplane.geodistance(track2[i],
#                                                                                              receiver.location)) * 10 / 3)
#     # print(track[i+1]-track[i]-0.5*100000000)
#     # print(airplane.geodistance(point[i+1],receiver.location) - airplane.geodistance(point[i],receiver.location))
#
# plt.plot(time_error, '.')
# plt.show()
