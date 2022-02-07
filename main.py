
############################################################
#import general
import pycom
import time
import machine
import sys
import os
import math
#import lib

from time import sleep
from L76GNSS import L76GNSS
from machine import Pin, I2C
from machine import rng
from machine import temperature
from machine import deepsleep
from machine import freq
from pycoproc_2 import Pycoproc
from machine import UART
from machine import unique_id


def init():
    pycom.heartbeat(False)
    print(freq())
    print(i2c.scan())
    print("hello")
    print("")

def blink():
    pycom.rgbled(0x030000)  # Red
    sleep(0.5)
    pycom.rgbled(0x00003)  # Blue
    sleep(0.5)

def data():
    #capteur b'\x10R\x1ce\xc2('
    id1 = unique_id()
    long1 = 2.5832759240614016
    lat1 = 48.841149870187856
    temp1 = ((machine.temperature() - 32) / 1.8)+7.0
    humidity1 = rng()/math.pow(2,18)
    press1 = rng()/2000
    #capteur b'\xb2R\x02e\xef('
    id2 = b'\xb2R\x02e\xef('
    long2 = 2.5896994123292316
    lat2 = 48.84058390450541
    temp2 = ((machine.temperature() - 32) / 1.8)
    humidity2 = rng()/math.pow(2,18)
    press2 = rng()/2000
    uart.write('id:{},lat:{},long:{},temperature:{},humidity:{},pressure:{},'.format(id1,lat1,long1,temp1,humidity1,press1)+'\n')
    #print('id:{},lat:{},long:{},temperature:{},humidity:{},pressure:{},'.format(id1,lat1,long1,temp1,humidity1,press1)+'\n')
    sleep(0.5)
    uart.write('id:{},lat:{},long:{},temperature:{},humidity:{},pressure:{},'.format(id2,lat2,long2,temp2,humidity2,press2)+'\n')
    #print('id:{},lat:{},long:{},temperature:{},humidity:{},pressure:{},'.format(id2,lat2,long2,temp2,humidity2,press2)+'\n')

py = Pycoproc()
L76 = L76GNSS(timeout=30, buffer=512)
i2c = L76.i2c
uart = UART(0, 9600)
init()

while True:
    blink()
    data()
    sleep(5)


    # py.setup_sleep(0.5)
    # py.go_to_sleep()
