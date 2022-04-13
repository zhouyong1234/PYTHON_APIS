#!/usr/bin/python
# -*-coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot  as plt

import matplotlib
myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')

filename = r'test.txt'
filepath = r'D:\wjh\audio_test\Music'


data = np.loadtxt('test.txt',dtype=int)

import sounddevice as sd
fs = 96000
src = data


sd.play(1*src/np.max(src), fs, blocking=True)

