#!/usr/bin/python
# -*-coding: utf-8 -*-

import cv2


cap = cv2.VideoCapture("/home/touchair/test/ground_640x480.mp4")
# 帧率
fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
# 分辨率-宽度
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# 分辨率-高度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# 总帧数
frame_counter = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

exposure_time = cap.get(5)

iso_speed = cap.get(cv2.CAP_PROP_ISO_SPEED)

cap.release()
cv2.destroyAllWindows()
# 时长，单位s
duration = frame_counter / fps

# print(fps)
# print(width)
# print(height)
# print(frame_counter)
# print(duration)
print(exposure_time)
# print(iso_speed)