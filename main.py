from receiver import Receiver  #接收器类
from airplane import Airplane  #飞机类
from attacker import Attacker  #攻击者类
from multiple import Multiple  #生成多条数据类
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #一架飞机
    airplane = Airplane('782034', [120, 30, 8500], [115, 28, 7500], 180, 0)

    track = airplane.track

    lng = []
    lat = []
    for position in track:
        # print(position)
        lng.append(position[0])
        lat.append(position[1])
    plt.plot(lng, lat, '.')
    plt.show()

    # # 一个接收器
    # receiver = Receiver([118, 32])
    #
    # # 一个位置固定的攻击者
    # attacker = Attacker([116, 30], 1)
    #
    # # 飞机的报文到接收器的时间轨迹
    # time_track_of_plane = receiver.fin_time_track(airplane)
    #
    # # 攻击者的报文到接收器的时间轨迹
    # time_track2 = receiver.ghost_time_track(attacker.ghost_list[0])
    #
    #
    # #生成多条航线例程
    # m = Multiple(30,10) #30条航线，10个接收器
    # m.match_RA() #一一对应航线和接收器
    # print(m.receiver_list[0]) #输出第一个接收器的所有信息
    # m.plt_all() #画出图像


