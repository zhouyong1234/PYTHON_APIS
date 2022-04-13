#!/usr/bin/python
# -*-coding: utf-8 -*-

# from cmath import nan
import serial
import threading
import binascii
from datetime import datetime
import struct
import csv
import time
import numpy as np



a = [[1,2,3], [4, np.nan, 6], [7,8,9]]
print(a[0].index(np.nan))
print(a[0:a.index(np.nan)])
print(a[a.index(np.nan)+1:len(a)])

# data_bytes=bytearray()


# def msg_list():
#     global data_bytes
#     # 新建一个列表
#     msg_list = list()
#     # 打开一个文件
#     r = "test.txt"
#     write_file = open(r, 'w')
#     # 配置串口名称、比特率、超时时间
#     port = '/dev/ttyACM0'
#     bps = 1536000
#     timex = 5
#     # 连接串口
#     ser = serial.Serial(port, bps, timeout=timex)
#     # print(ser)
#     # 等下时间，去启动串口发送程序
#     time.sleep(3)
#     # 进入读写过程

#     getBytes=b''




#     while True:
#         count = ser.inWaiting()

#         # print(count)

#         # if count > 0:

#         data = ser.read(2)
#         # if data != getBytes:

#         # print(data)

#         print(struct.unpack("<h", data)[0])
        
#         # print(hex(struct.unpack("<B", data)[0]).replace("0x",""))
#         # print(len(hex(struct.unpack("<B", data)[0]).replace("0x","")))
#         # if(len(hex(struct.unpack("<B", data)[0]).replace("0x","")) == 1):
#         #     write_file.write("0"+hex(struct.unpack("<B", data)[0]).replace("0x",""))
#         #     write_file.write(' ')
#         #     getBytes=data
#         # else:
#         # write_file.write(hex(struct.unpack("<B", data)[0]).replace("0x",""))
#         # write_file.write(' ')
#         # getBytes=data
#         write_file.write(str(struct.unpack("<h", data)[0]))
#         write_file.write('\n')

        
                
#         # else:
#         #     ser.close()
#         #     write_file.close()
#         #     break

# msg_list()

