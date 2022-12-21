import numpy as np
import serial as sr
s = sr.Serial('COM5',9600, timeout=1)
val = []

while True:
    line = s.readline()
    string = line.decode()
    # stripped_string = string.strip()
    num = string.split(",")
    x1 = int(num[0])
    x2 = int(num[1])

    print(x1)
    # print("\t")
    print(x2)