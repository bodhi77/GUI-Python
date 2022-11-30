import serial
import time
import numpy
import matplotlib.pyplot as plt
from drawnow import *


tempF = []
pressure = []

arduinoData = serial.Serial('/dev/ttyACM0',115200)
plt.ion()       #Tell matplotlib you want interactive mode to plot live data
cnt = 0

def makeFig():              # Create a function that makes our desired plot
    #plt.ylim(490,530)         # Menambahkan limit sumbu y
    plt.title('My Live Streaming Sensor Data')
    plt.grid(True)          # Tambahkan grid
    plt.ylabel('Temp F')    # Tambahkan label
    plt.plot(tempF, 'ro-', label='Degrees F')
    plt.legend(loc='upper left')
    plt2 = plt.twinx()
    plt2.plot(pressure, 'b^-')


while True:
    while (arduinoData.inWaiting()==0):
        pass
    arduinoString = arduinoData.readline()
    dataString = arduinoString.decode('utf-8')
    data=dataString[0:][:-2]
    dataArray = data.split(',')
    temp = float (dataArray[0])
    P = float (dataArray[1])
    #print temp,",",P   # cek data sudah bisa di-split atau belum
    tempF.append(temp)
    pressure.append(P)
    #print tempF        # cek append sudah bisa atau belum
    drawnow(makeFig)    # Call drawnow to update our live graph
    plt.pause(.000001)
    cnt = cnt + 1
    if(cnt > 50):       # setting sumbu x = 50, agar data tidak menumpuk
        tempF.pop(0)
        pressure.pop(0)