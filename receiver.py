from airplane import Airplane
from attacker import Attacker
import matplotlib.pyplot as plt
import random

class Receiver():
    def __init__(self, location):
        '''
        :param location: [lng,lat] 接收器坐标
        '''
        self.location = location
        self.airplane_dic = {}
        self.ghost_dic = {}

    # 噪声
    def nosie(self):
        # 高斯白噪声
        return random.uniform(-200,200)

    # 飞机与地面接收器的时钟漂移
    def drift(self, dirfting):
        '''
        :param dirfting: 每0.5秒钟漂移的纳秒数
        :return:
        '''
        return dirfting+random.uniform(0,dirfting/3)

    # 获取最终的接收时间轨迹
    def fin_time_track(self,airplane):
        '''
        :param airplane: Airplane
        :return:
        '''
        time_track=[]
        track = airplane.gettrack()
        last_time = airplane.starttime*1000000000
        # last_time = 0
        for position in track:
            # 到达时间 = 上一条消息发出的时间+0.5+漂移+噪音+信号飞行时间
            time_of_arrive = (last_time+0.5*100000000)+self.drift(500) + self.nosie() + airplane.geodistance(position,self.location)*10/3
            # time_of_arrive = self.drift(200) + self.nosie()+ airplane.geodistance(position,self.location)*10/3
            last_time = time_of_arrive - airplane.geodistance(position,self.location)*10/3
            time_track.append(time_of_arrive)
        self.airplane_dic[airplane.icao] = tuple(time_track)
        airplane.time_track = time_track
        return time_track


    def ghost_time_track(self, ghost):
        '''
        :param ghost:
        :return:time_track
        '''

        time_track = []
        track = ghost.track
        # track = attacker.get_ghost().track
        last_time = ghost.starttime * 1000000000
        # last_time = 0
        for position in track:
            # 到达时间 = 上一条消息发出的时间+0.5+漂移+噪音+信号飞行时间
            time_of_arrive = (last_time + 0.5 * 100000000) + self.drift(200) + self.nosie() + airplane.geodistance(
                ghost.ghost_flag, self.location) * 10 / 3
            # time_of_arrive = self.drift(200) + self.nosie()+ airplane.geodistance(position,self.location)*10/3
            last_time = time_of_arrive - airplane.geodistance(position, self.location) * 10 / 3
            time_track.append(time_of_arrive)
        self.ghost_dic[ghost.icao] = tuple(time_track)
        ghost.time_track = time_track
        return time_track


    # 绘制接收器与飞机轨迹坐标图
    def plt_location(self,airplane):
        track = airplane.gettrack()
        lng = []
        lat = []
        for position in track:
            lng.append(position[0])
            lat.append(position[1])
        plt.plot(lng,lat,'.')
        plt.plot(self.location[0], self.location[1],'r.')
        plt.show()


# receiver = Receiver([118,32])
# attacker = Attacker([116,30],1)
# airplane = Airplane('782034',[120,30],[115,28],180,0)#1564503340
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
