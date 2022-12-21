from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import serial as sr
import time

data1 = np.array([])
data2 = np.array([])
data3 = np.array([])
cond = False

# --- Start Serial ---
s = sr.Serial('COM5',9600, timeout=1)
time.sleep(2)
s.reset_input_buffer()

# -- Plot Data --
def plot_data():
    global cond,data1,data2,data3
    if (cond==True):
        a = s.readline()
        string = a.decode()
        p = string.split(",")
        x1 = float(p[0])
        x2 = float(p[1])
        x3 = float(p[2])

        if(len(data1) < 100):
            data1 = np.append(data1,x1)
        else:
            data1[0:99] = data1[1:100]
            data1[99] = x1
        
        if(len(data2) < 100):
            data2 = np.append(data2,x2)
        else:
            data2[0:99] = data2[1:100]
            data2[99] = x2
        
        if(len(data3) < 100):
            data3 = np.append(data3,x3)
        else:
            data3[0:99] = data3[1:100]
            data3[99] = x3

        # data1 = np.append(data1, float(p[0]))
        # data2 = np.append(data2, float(p[1]))

        lines1.set_xdata(np.arange(0,len(data1)))
        lines1.set_ydata(data1)
        lines2.set_xdata(np.arange(0,len(data2)))
        lines2.set_ydata(data2)
        lines3.set_xdata(np.arange(0,len(data3)))
        lines3.set_ydata(data3)
        print(x1)
        # print("/n")
        print(x2)
        print(x3)

        canvas1.draw()
        canvas2.draw()

    root.after(1,plot_data)

def plot_start():
    global cond
    cond = True
    s.reset_input_buffer()

def plot_stop():
    global cond
    cond = False

root = tk.Tk()
root.title('Real Time Plot')
root.configure(background= 'light blue')
root.geometry("1400x900")

## -- Create Plot object on GUI --
fig1 = Figure()
fig2 = Figure()

## Subplot Setpoint
ax = fig1.add_subplot(111)
ax.set_title("Serial Data")
ax.set_xlabel("Time")
ax.set_ylabel("Setpoint")
ax.set_xlim(0,100)
ax.set_ylim(0,360)
lines1 = ax.plot([],[])[0]
lines2 = ax.plot([],[])[0]

# Subplot Error
ax2 = fig2.add_subplot(111)
ax2.set_title("Error")
ax2.set_xlabel("Time")
ax2.set_ylabel("Value")
ax2.set_xlim(0,100)
ax2.set_ylim(-50,50)
lines3 = ax2.plot([],[])[0]

canvas1 = FigureCanvasTkAgg(fig1, master=root)
canvas1.get_tk_widget().place(x=50,y=200,width=600,height=400)
canvas1.draw()

canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas2.get_tk_widget().place(x=700,y=200,width=600,height=400)
canvas2.draw()

## -- Create Button --
root.update()
start = tk.Button(root, text="Start", font=('Arial',12), command = lambda: plot_start())
start.place(x=100,y=630)

root.update()
stop = tk.Button(root, text="Stop", font=('Arial',12), command = lambda: plot_stop())
stop.place(x=start.winfo_x()+start.winfo_reqwidth()+40, y=630)

root.after(1,plot_data)
root.mainloop()