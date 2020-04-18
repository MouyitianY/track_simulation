from airplane import Airplane
from receiver import Receiver
import random
import matplotlib.pyplot as plt

class Multiple:
    def __init__(self, plane_num, receiver_num):
        self.plane_list = []
        self.get_random_airplane(plane_num)
        self.receiver_list = []
        self.get_random_receiver(receiver_num)


    def get_random_airplane(self, plane_num):
        '''
        :param: num
        :return: plane_list: [Airplane,...] 飞机列表
        '''
        plane_list = []
        for i in range(plane_num):
            # 随机生成icao、start、end、speed、starttime
            icao = random.randint(700000, 799999)
            start = [random.uniform(115, 125),random.uniform(28, 34)]
            end = [start[0] + random.uniform(-3, 3), start[1] + random.uniform(-3, 3)]
            speed = random.randint(150, 300)
            starttime = random.randint(1000, 16000)
            # 根据随机数据生成飞机
            plane = Airplane(str(icao), start, end, speed, starttime)

            # 放入plane库中
            # plane_list.append(plane)
            self.plane_list.append(plane)
        # return ghost
        return plane_list

    def get_random_receiver(self,receiver_num):
        '''
        :param receiver_num: int
        :return:
        '''
        for i in range(receiver_num):
            location = [random.uniform(115, 125),random.uniform(28, 34)]
            receiver = Receiver(location)
            self.receiver_list.append((receiver))

    def match_RA(self):
        '''
        :param R_num: 接收器数量
        :param A_num: 飞机数量
        :return:
        '''
        R_num = len(self.receiver_list)
        A_num = len(self.plane_list)
        for i in range(R_num):
            receiver = self.receiver_list[i]
            for j in range(A_num):
                plane = self.plane_list[j]
                if plane.geodistance(receiver.location, plane.start) < 300000 \
                        or plane.geodistance(receiver.location, plane.destination) < 300000:
                    receiver.fin_time_track(plane)

    def plt_all(self):
        for i in range(len(self.plane_list)):
            track = self.plane_list[i].gettrack()
            lng = []
            lat = []
            for position in track:
                lng.append(position[0])
                lat.append(position[1])
            plt.plot(lng, lat, '.')

        for i in range(len(self.receiver_list)):
            plt.plot(self.receiver_list[i].location[0], self.receiver_list[i].location[1], 'r.')

        plt.show()


# m = Multiple(30,10)
# m.match_RA()
# print(m.receiver_list[0])
# m.plt_all()
#
# A = m.plane_list[0]
# for i in range(10):
#     if A.icao in m.receiver_list[i].airplane_dic:
#         plt.plot(m.receiver_list[i].airplane_dic[A.icao])
#
# plt.show()

