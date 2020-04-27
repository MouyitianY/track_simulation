from math import radians, cos, sin, asin, sqrt, pi, atan, pow
import random

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
        self.track = self.gettrack()



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

    def get_ghost_flag(self, ghost_flag):
        '''
        :param ghost_flag: location [lng,lat]
        :return:
        '''
        self.ghost_flag = ghost_flag



