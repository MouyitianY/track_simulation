from math import radians, cos, sin, asin, sqrt, pi, atan, pow
import random
import numpy as np
from scipy.interpolate import  Akima1DInterpolator
import matplotlib.pyplot as plt

class Airplane:
    def __init__(self, icao, start, destination, speed, starttime):
        '''
        :param icao:'AAAAAA'飞机标识号
        :param start: [lng,lat，high]起点
        :param destination:[lng, lat，high]终点
        :param speed:m/s速度
        :param starttime: s开始时间
        '''
        self.icao = icao
        self.start = start
        self.destination = destination
        self.speed = speed
        self.starttime = starttime
        # self.distance = self.geodistance(start,destination)
        self.angle = self.azimuthAngle(start,destination)
        # self.alltime = self.distance/self.speed
        self.time_track = [] #在接收器端执行对应的函数后产生（）
        self.track = self.gettrack_insert()



    # 公式计算两点间距离（m）
    def geodistance(self, start, destination):
        lng1, lat1, high1, lng2, lat2, high2 = start[0],start[1],start[2],destination[0],destination[1],destination[2]
        lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])  # 经纬度转换成弧度
        dlon = lng2 - lng1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        distance = 2 * asin(sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
        distance = round(distance, 3)
        high_diff = high1-high2
        distance = sqrt(pow(distance,2)+pow(high_diff,2))
        return distance

    # 计算方向角
    def azimuthAngle(self, start, destination):
        x1, y1, x2, y2 = start[0], start[1], destination[0], destination[1]
        angle = 0.0;
        dx = x2 - x1
        dy = y2 - y1
        if x2 == x1:
            angle = pi / 2.0
            if y2 == y1:
                angle = 0.0
            elif y2 < y1:
                angle = 3.0 * pi / 2.0
        elif x2 > x1 and y2 > y1:
            angle = atan(dx / dy)
        elif x2 > x1 and y2 < y1:
            angle = pi / 2 + atan(-dy / dx)
        elif x2 < x1 and y2 < y1:
            angle =pi + atan(dx / dy)
        elif x2 < x1 and y2 > y1:
            angle = 3.0 * pi / 2.0 + atan(dy / -dx)
        return (angle * 180 / pi)

    # 获取航线轨迹坐标列表 [[lng,lat]...]
    def gettrack(self):
        track = []
        # 起点和终点的差值
        error = [self.destination[0] - self.start[0], self.destination[1] - self.start[1]]

        # 根据经纬度范围随机生成拐点数量
        # point_num = 0
        point_num = random.randint(min(abs(int(error[0])*3),abs(int(error[1]))*3),max(abs(int(error[0])*3),abs(int(error[1]))*3))
        # point_num = random.randint(10,20)
        # print(point_num)
        offset_point_set = [self.start]



        # 生成【0，1】之间的随机序列
        rand_set = [0,1]
        for i in range(int(point_num)):
            rand_set.append(random.random())
        rand_set.sort()

        # 生成拐点
        for i in range(point_num):

            offset_point = [self.start[0]+error[0]*(rand_set[i+1]+(rand_set[i+2]-rand_set[i+1])*random.uniform(-1,1)),
                            self.start[1]+error[1]*rand_set[i+1],
                            offset_point_set[i][2]+random.randint(-10,10)*100]
            # 拐点=直线点+误差

            offset_point_set.append(offset_point)
        offset_point_set.append(self.destination)
        # print(offset_point_set)

        # 两两拐点生成直线
        for i in range(len(offset_point_set)-1):
            error = [offset_point_set[i+1][0]-offset_point_set[i][0],
                     offset_point_set[i+1][1]-offset_point_set[i][1],
                     (offset_point_set[i+1][2]-offset_point_set[i][2])//50]


            cost_time = self.geodistance(offset_point_set[i+1], offset_point_set[i])/self.speed
            massage_num = cost_time // 0.5
            massage_num = int(massage_num)
            # print(massage_num)
            for j in range(massage_num):
                position = [offset_point_set[i][0]+error[0]*j/(massage_num),
                            offset_point_set[i][1]+error[1]*j/(massage_num),
                            offset_point_set[i][2]+(error[2]*(j/(massage_num)))//1*50]
                track.append(position)
        return track


    # 插值法获得轨迹
    def gettrack_insert(self):
        track = []
        # 起点和终点的差值
        error = [self.destination[0] - self.start[0], self.destination[1] - self.start[1]]

        # 根据经纬度范围随机生成拐点数量
        point_num = random.randint(min(abs(int(error[0])*2),abs(int(error[1]))*2),max(abs(int(error[0])*2),abs(int(error[1]))*2))
        if point_num <= 0:
            point_num = 1
        # point_num = random.randint(10,20)
        # print(point_num)
        offset_point_set = [self.start]

        # 生成[0，1]之间的随机序列
        rand_set = [0,1]
        for i in range(int(point_num)):
            rand_set.append(random.random())
        rand_set.sort()

        # 生成拐点
        for i in range(point_num):
            offset_point = [self.start[0]+error[0]*rand_set[i+1],
                            self.start[1]+error[1]*(rand_set[i+1]+(rand_set[i+2]-rand_set[i+1])*random.uniform(-1,1)),
                            offset_point_set[i][2]+random.randint(-10,10)*100]
            # 拐点=直线点+误差
            offset_point_set.append(offset_point)
        offset_point_set.append(self.destination)
        # print(offset_point_set)

        # 使用拐点生成曲线
        reverse_flag = 0  #递增标志
        # 数据化为递增序列
        if offset_point_set[0][0]>offset_point_set[-1][0]:
            offset_point_set.reverse()
            reverse_flag = 1

        # akima插值法
        # 提取数据
        x_data = []
        y_data = []
        h_data = []
        for i in offset_point_set:
            x_data.append(i[0])
            y_data.append(i[1])
            h_data.append(i[2])
        x_data = np.array(x_data)
        y_data = np.array(y_data)
        h_data = np.array(h_data)
        h_range = rand_set
        h_range = np.array(h_range)

        # 按照距离对x进行分段
        x_data_smooth = [0]
        hx_data_smooth = [0]
        for i in range(len(offset_point_set)-1):
            massage_num = (self.geodistance(offset_point_set[i],offset_point_set[i+1]))*2/self.speed + 1
            x_data_smooth = x_data_smooth[:-2] + \
                            list(np.linspace(offset_point_set[i][0],offset_point_set[i+1][0], massage_num))
            hx_data_smooth = hx_data_smooth[:-2] + \
                            list(np.linspace(h_range[i], h_range[i + 1], massage_num))

        # 插值
        bi = Akima1DInterpolator(x_data, y_data)
        x_data_smooth = np.array(x_data_smooth)
        # print(x_data_smooth)
        y_data_smooth = bi(x_data_smooth)

        bi = Akima1DInterpolator(h_range, h_data)
        h_data_smooth = bi(hx_data_smooth)

        for i in range(len(x_data_smooth)):
            track.append([x_data_smooth[i], y_data_smooth[i], h_data_smooth[i]])

        # x = []
        # y = []
        # for i in track:
        #     x.append(i[0])
        #     y.append(i[1])
        # plt.plot(x, y, '.')
        # for i in offset_point_set:
        #     plt.plot(i[0], i[1], 'ro', label="point")
        # plt.show()
        if reverse_flag == 1:
            track.reverse()
        return track

    def get_ghost_flag(self, ghost_flag):
        '''
        :param ghost_flag: location [lng,lat]
        :return:
        '''
        self.ghost_flag = ghost_flag




# airplane = Airplane('782034', [120.1549, 30, 8500], [115, 28.15455, 7500], 180, 0)
# x=[]
# y =[]
# for i in airplane.track:
#     x.append(i[2])
# #     y.append(i[1])
# plt.plot(x,'.')
# plt.show()
