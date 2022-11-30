#Source: https://www.learnrobotics.org/blog/arduino-data-logger-csv/
#modifed by Bodhi Setiawan

import serial
import time
import csv
import matplotlib.pyplot as plt

list_collumn = ["xnf","xf","ynf","yf","znf","zf"]
samples = 105 #jumlah sampel/cuplikan yang ingin diambil
print_labels = False
line = 0 #line dimulai dari 0
sensor_data = [] #store data

arduino_port = "/dev/ttyACM0" #serial port pada Arduino
baud = 115200 #atur baudrate
fileName="alpha0.9.csv" #nama file

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)
file = open(fileName, "a")
print("Created file")

#menampilkan data ke terminal

getData=ser.readline()
dataString = getData.decode('utf-8')
data=dataString[0:][:-2]
print(data)

readings = data.split(",")
print(readings)

sensor_data.append(readings)
print(sensor_data)

# mengambil sampel
while line <= samples:
    getData=ser.readline()
    dataString = getData.decode('utf-8')
    data=dataString[0:][:-2]
    print(data)

    readings = data.split(",")
    print(readings)

    sensor_data.append(readings)
    print(sensor_data)

    line = line+1
    time.sleep(0.01)
   
# membuat file CSV (format file bisa diganti ke xlsx di bagian nama file)
with open(fileName, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(list_collumn)
    writer.writerows(sensor_data)

print("Data collection complete!")
file.close()
