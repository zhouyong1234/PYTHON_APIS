#!/usr/bin/python
# -*-coding: utf-8 -*-

import serial
import threading
import binascii
from datetime import datetime
import struct
import csv
import time

data_bytes=bytearray()


r = "test_video_11.05.txt"
write_file = open(r, 'w')


def msg_list():
    global data_bytes
    # 新建一个列表
    msg_list = list()
    # 打开一个文件
    r = "/home/touchair/test/video_11.05.txt"
    with open(r, "r") as f:
        # print(f.readline())
        while True:
            chunk = f.read(2)

            print(struct.unpack("<h", chunk)[0])

            write_file.write(str(struct.unpack("<h", chunk)[0]))
            write_file.write('\n')

            if not chunk:
                break

msg_list()

