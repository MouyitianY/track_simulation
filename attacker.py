import random
from airplane import Airplane


class Attacker:
    def __init__(self,location,ghost_num):
        # self.track = airplane.gettrack()
        self.loaction = location
        # 初始化ghost库
        # 用列表做ghost plane仓库
        self.ghost_list = []
        self.ghost_list = self.get_random_ghost(ghost_num)

    # 随机生成幽灵飞机
    def get_random_ghost(self,ghost_num):
        '''
        :param: ghost_num
        :return: ghost_list: [Airplane,...] 幽灵飞机列表
        '''
        ghost_list = []
        for i in range(ghost_num):
            # 随机生成icao、start、end、speed、starttime
            icao = random.randint(700000, 799999)
            start = [self.loaction[0] + random.uniform(-3, 3), self.loaction[1] + random.uniform(-3, 3), 5000+random.randint(-10,10)*50]
            end = [self.loaction[0] + random.uniform(-3, 3), self.loaction[1] + random.uniform(-3, 3), 5000+random.randint(-10,10)*50]
            speed = random.randint(150, 300)
            starttime = random.randint(1000, 16000)
            # 根据随机数据生成飞机
            ghost = Airplane(str(icao), start, end, speed, starttime)
            # 标记为ghost，且放入发射器位置
            ghost.get_ghost_flag(self.loaction)
            # 放入ghost库中
            ghost_list.append(ghost)
            self.ghost_list.append(ghost)
        # return ghost
        return ghost_list



# att = Attacker([1,1])
# print(att.ghost_list)
# att.get_random_ghost(2)
# print(att.ghost_list)

