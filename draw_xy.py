#!/usr/bin/python
# -*-coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
#从pyplot导入MultipleLocator类，这个类用于设置刻度间隔



gnss_filename = '/home/touchair/test/data/LY1_pass.txt'


data_list = []
x = []
y = []


gnss_f = open(gnss_filename, "r") 
lines = gnss_f.readlines()      
for line in lines:
    # print(float(line.split(",")[0]), float(line.split(",")[1]))

    # origin = [float(line.split(",")[0]), float(line.split(",")[1]), float(line.split(",")[2])]
    # rotate = np.dot(rot_matrix, origin)

    x.append(float(line.split(",")[0]))
    y.append(float(line.split(",")[1]))

print(np.var(x), np.std(x))
print(np.var(y), np.std(y))




# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [1.07474e-04, 4.30044e-04, 9.67937e-04, 1.72137e-03, 2.69058e-03, 3.87577e-03, 5.27716e-03, 6.89499e-03, 8.72945e-03, 0.0107808]

# x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [1.98492, 1.92118, 1.71899, 1.31314, 1.38148, 1.07808, 7.36608e-01, 5.33269e-01, 5.90244e-01]
 
fig = plt.figure("gps_cam", [16, 12])
plt.plot(x, y, c='green', label='uppc')
# plt.scatter(x, y)
# plt.tick_params(axis='both',which='major',labelsize=14)
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)
# x_major_locator=MultipleLocator(1)
# #把x轴的刻度间隔设置为1，并存在变量里
# y_major_locator=MultipleLocator(0.2)
# #把y轴的刻度间隔设置为10，并存在变量里
# ax=plt.gca()
# #ax为两条坐标轴的实例
# ax.xaxis.set_major_locator(x_major_locator)
# #把x轴的主刻度设置为1的倍数
# ax.yaxis.set_major_locator(y_major_locator)
# #把y轴的主刻度设置为10的倍数
# plt.xlim(2, 10)
# #把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
# plt.ylim(5.33269e-01, 1.98492)
# #把y轴的刻度范围设置为-5到110，同理，-5不会标出来，但是能看到一点空白
plt.legend()

plt.savefig('uppc.png') #路径+文件名

plt.show()

