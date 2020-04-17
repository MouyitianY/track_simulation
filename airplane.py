from math import radians, cos, sin, asin, sqrt, pi, atan

class Airplane:
    def __init__(self, icao, start, destination, speed, starttime):
        '''
        :param icao:'AAAAAA'飞机标识号
        :param start: [lng,lat]起点
        :param destination:[lng, lat]终点
        :param speed:m/s速度
        :param starttime: s开始时间
        '''
        self.icao = icao
        self.start = start
        self.destination = destination
        self.speed = speed
        self.starttime = starttime
        self.distance = self.geodistance(start,destination)
        self.angle = self.azimuthAngle(start,destination)
        self.alltime = self.distance/self.speed
        self.time_track = [] #在接收器端执行对应的函数后产生（）
        self.track = self.gettrack()



    # 公式计算两点间距离（m）
    def geodistance(self, start, destination):
        lng1, lat1, lng2, lat2 = start[0],start[1],destination[0],destination[1]
        lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])  # 经纬度转换成弧度
        dlon = lng2 - lng1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        distance = 2 * asin(sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
        distance = round(distance, 3)
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
        error = [self.destination[0]-self.start[0],self.destination[1]-self.start[1]]

        massage_num = self.alltime // 0.5
        massage_num = int(massage_num)
        for i in range(massage_num):
            position = [self.start[0]+error[0]*i/(massage_num), self.start[1]+error[1]*i/(massage_num)]
            track.append(position)
        return track

    def get_ghost_flag(self, ghost_flag):
        '''
        :param ghost_flag: location [lng,lat]
        :return:
        '''
        self.ghost_flag = ghost_flag



# airplane = Airplane([120.128234,30.2141348],[115.86143245,28.750012],180)
# airplane2 = Airplane([120.128234,30.2141348],[(120.128234+115.86143245)/2,(28.750012+30.2141348)/2],180)
# print(airplane.distance,airplane.angle,airplane.alltime,airplane.gettrack())
# print(airplane2.distance,airplane2.alltime)