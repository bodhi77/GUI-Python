import serial
import time
import numpy as np

import tkinter as tk
import tkinter.ttk as ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from drawnow import *


root = tk.Tk()#ウインドの作成 gawe jendela
root.title("pid soft")#ウインドのタイトル gawe judul jendela
root.geometry("650x350") #ウインドの大きさ ukurane jendela
frame_1 = tk.LabelFrame(root,labelanchor="nw",text="グラフ",foreground="green")
frame_1.grid(rowspan=2, column=0)
frame_2 = tk.LabelFrame(root,labelanchor="nw",text="パラメータ",foreground="green")
frame_2.grid(row=0, column=1, sticky="nwse")
frame3=tk.LabelFrame(root,text="履歴",foreground="green")
frame3.grid(row=1,column=1,sticky="nwse")


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
    # drawnow(makeFig)    # Call drawnow to update our live graph
    canvas = FigureCanvasTkAgg(drawnow(makeFig), master=frame_1)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    plt.pause(.000001)
    cnt = cnt + 1
    if(cnt > 50):       # setting sumbu x = 50, agar data tidak menumpuk
        tempF.pop(0)
        pressure.pop(0)