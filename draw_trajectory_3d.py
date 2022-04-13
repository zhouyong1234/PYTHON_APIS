#!/usr/bin/python
# -*-coding: utf-8 -*-

from asyncore import file_wrapper
from cProfile import label
from fileinput import filename
from operator import ipow, le
import matplotlib.pyplot as plt
import numpy as np
import math 
import scipy.linalg as linalg
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D 


def rotate_mat(axis, radian):
    rot_matrix = linalg.expm(np.cross(np.eye(3), axis / linalg.norm(axis) * radian))
    return rot_matrix


axis_x, axis_y, axis_z = [1,0,0], [0,1,0], [0,0,1]
rand_axis = [0,0,1]

# yaw = math.pi / 9.6
yaw = math.pi
rot_matrix = rotate_mat(rand_axis, yaw)


gnss_filename = '/home/touchair/test/fusion_gps.txt'
cam_filename = '/home/touchair/test/fusion_state.txt'

data_list = []
gnss_x = []
gnss_y = []
gnss_z = []


fusion_x = []
fusion_y = []
fusion_z = []

gnss_f = open(gnss_filename, "r") 
lines = gnss_f.readlines()      
for line in lines:
    # print(float(line.split(",")[0]), float(line.split(",")[1]))

    # origin = [float(line.split(",")[0]), float(line.split(",")[1]), float(line.split(",")[2])]
    # rotate = np.dot(rot_matrix, origin)

    gnss_x.append(float(line.split(",")[0]))
    gnss_y.append(float(line.split(",")[1]))
    gnss_z.append(float(line.split(",")[2]))

    # x.append(rotate[0])
    # y.append(rotate[1])




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

    fusion_x.append(float(line.split(",")[0]))
    fusion_y.append(float(line.split(",")[1]))
    fusion_z.append(float(line.split(",")[2]))
    # z.append(rotate[0])
    # w.append(rotate[1])


fig = plt.figure("gps_cam", figsize=[20,16])

ax = plt.axes(projection='3d')
# 三维线的数据

ax.plot3D(gnss_x, gnss_y, gnss_z, 'green', label='gps')
ax.plot3D(fusion_x, fusion_y, fusion_z, 'red', label='fusion')
# 三维散点的数据
# zdata = 15 * np.random.random(100)
# xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
# ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
# ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
plt.legend()
plt.show()




