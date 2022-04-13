#!/usr/bin/python
# -*-coding: utf-8 -*-

from asyncore import file_wrapper
from fileinput import filename
from operator import ipow, le
import matplotlib.pyplot as plt
import numpy as np
import math 
import scipy.linalg as linalg
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D 


# 定义计算离散点导数的函数
def cal_deriv(x, y):                  # x, y的类型均为列表
    diff_x = []                       # 用来存储x列表中的两数之差
    for i, j in zip(x[0::], x[1::]):  
        diff_x.append(j - i)
 
    diff_y = []                       # 用来存储y列表中的两数之差
    for i, j in zip(y[0::], y[1::]):
        diff_y.append(j - i)  
        
    slopes = []                       # 用来存储斜率
    for i in range(len(diff_y)):
        slopes.append(diff_y[i] / diff_x[i])
        
    deriv = []                        # 用来存储一阶导数
    for i, j in zip(slopes[0::], slopes[1::]):        
        deriv.append((0.5 * (i + j))) # 根据离散点导数的定义，计算并存储结果
    deriv.insert(0, slopes[0])        # (左)端点的导数即为与其最近点的斜率
    deriv.append(slopes[-1])          # (右)端点的导数即为与其最近点的斜率
 
    # for i in deriv:                   # 打印结果，方便检查，调用时也可注释掉
    #     print(i)
 
    return deriv                      # 返回存储一阶导数结果的列表


def cal_2nd_deriv(x,y):
    return cal_deriv(x, cal_deriv(x, y))



def rotate_mat(axis, radian):
    rot_matrix = linalg.expm(np.cross(np.eye(3), axis / linalg.norm(axis) * radian))
    return rot_matrix


axis_x, axis_y, axis_z = [1,0,0], [0,1,0], [0,0,1]
rand_axis = [0,0,1]

# yaw = math.pi / 9.6
yaw = math.pi
rot_matrix = rotate_mat(rand_axis, yaw)
# print(rot_matrix)


# filename = '/home/touchair/test/LY2_pass.txt'
# filename = '/home/touchair/test/LY1(1).txt'
# filename = '/home/touchair/test/LY1_pass.txt'
# filename = '/home/touchair/test/LY2.txt'
# gnss_filename = '/home/touchair/test/data/gnss_imu/gnss.txt'
# cam_filename = '/home/touchair/test/data/gnss_imu/vins_result_loop.txt'

gnss_filename = '/home/touchair/test/data/fusion_gps.txt'
cam_filename = '/home/touchair/test/data/fusion_state.txt'

data_list = []
x = []
y = []
z = []
w = []




gnss_f = open(gnss_filename, "r") 
lines = gnss_f.readlines()      
for line in lines:
    # print(float(line.split(",")[0]), float(line.split(",")[1]))

    # origin = [float(line.split(",")[0]), float(line.split(",")[1]), float(line.split(",")[2])]
    # rotate = np.dot(rot_matrix, origin)

    x.append(float(line.split(",")[0]))
    y.append(float(line.split(",")[1]))

    # x.append(rotate[0])
    # y.append(rotate[1])

# print(len(x), len(y))
# print(cal_2nd_deriv(x,y))
print(len(cal_2nd_deriv(x,y)))


cam_f = open(cam_filename, "r") 
lines = cam_f.readlines()      
for line in lines:
    # print(float(line.split(",")[0]), float(line.split(",")[1]))
    # origin = [float(line.split(",")[2])*9, -float(line.split(",")[0])*9, float(line.split(",")[1])*9]
    # origin = [float(line.split(",")[2])*35, -float(line.split(",")[0])*35, float(line.split(",")[1])*35]
    # print(origin)
    # rotate = np.dot(rot_matrix, origin)
    # print(rotate)

    # origin = [float(line.split(",")[0]), float(line.split(",")[1]), float(line.split(",")[2])]
    # # rotate = np.dot(rot_matrix, origin)
    # rotate = origin

    z.append(float(line.split(",")[0]))
    w.append(float(line.split(",")[1]))
    # z.append(rotate[0])
    # w.append(rotate[1])

# print(len(z), len(w))
# print(cal_2nd_deriv(z,w))
print(len(cal_2nd_deriv(x,w)))


# print("平均值为：%f " % np.mean(data_list))
# print("方差为：%f" % np.var(data_list))
# print("标准差为: %f" % np.std(data_list, ddof=1))



# for index, value in enumerate(data_list):
#     x.append(index)
#     y.append(value)
#     z.append(np.mean(data_list))
#     w.append(np.var(data_list))



# # plt.title("loss function")
# # plt.xlabel("running times")
# # plt.ylabel("loss value")
# # plt.plot(x, y, label="loss")
# # plt.legend()
# # plt.show()

# import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
# #从pyplot导入MultipleLocator类，这个类用于设置刻度间隔

fig = plt.figure("gps_cam", [16, 12])



# plt.plot(np.arange(0,570), cal_2nd_deriv(x,y), c='green', label='gps', linewidth=1.2)
# plt.plot(np.arange(0,570), cal_2nd_deriv(z,w), c='red', label='fusion', linewidth=1.2)
# plt.xlim(0, 570)


########################################################################################
# plt.subplot(211)
plt.plot(x, y, c='green', label='gps', linewidth=1.2)
# plt.scatter(x, y, s=20, c='r', label="gnss")
# plt.legend()

# plt.subplot(212)
plt.plot(z, w, c='red', label='fusion', linewidth=1.2)
# plt.scatter(z, w, s=20, c='b', label="cam")
# plt.plot(x, z, c='red', label='mean: {}'.format(round(np.mean(data_list), 2)))
# plt.plot(x, w, c='blue', label='var: {}'.format(round(np.var(data_list), 5)))
# plt.title('Truth: 2.5m',fontsize=16)
# plt.tick_params(axis='both',which='major',labelsize=14)
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)
x_major_locator=MultipleLocator(30)
# #把x轴的刻度间隔设置为1，并存在变量里
y_major_locator=MultipleLocator(30)
# #把y轴的刻度间隔设置为10，并存在变量里
ax=plt.gca()
# #ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
# #把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)
# #把y轴的主刻度设置为10的倍数
plt.xlim(-120, 60)
# #把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
plt.ylim(-250, 20)
# #把y轴的刻度范围设置为-5到110，同理，-5不会标出来，但是能看到一点空白
# plt.colorbar()
########################################################################################



plt.legend()

# plt.savefig('diff.png') #路径+文件名

plt.show()





