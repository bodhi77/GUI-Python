from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import serial as sr
import time

data1 = np.array([])
data2 = np.array([])
cond = False

# --- Start Serial ---
s = sr.Serial('COM5',9600, timeout=1)
time.sleep(2)
s.reset_input_buffer()

# -- Plot Data --
def plot_data():
    global cond,data1,data2
    if (cond==True):
        a = s.readline()
        string = a.decode()  # convert the byte string to a unicode string
        # stripped_string = string.strip()
        # num = float(stripped_string)
        p = string.split(",")
        x1 = int(p[0])
        x2 = int(p[1])

        if(len(data1) < 100):
            data1 = np.append(data1,float(p[0]))
        else:
            data1[0:99] = data1[1:100]
            data1[99] = float(p[0])
        
        if(len(data2) < 100):
            data2 = np.append(data2,float(p[1]))
        else:
            data2[0:99] = data2[1:100]
            data2[99] = float(p[1])

        # data1 = np.append(data1, float(p[0]))
        # data2 = np.append(data2, float(p[1]))

        lines1.set_xdata(np.arange(0,len(data1)))
        lines1.set_ydata(data1)
        lines2.set_xdata(np.arange(0,len(data2)))
        lines2.set_ydata(data2)
        print(x1)
        # print("/n")
        print(x2)

        canvas.draw()

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
root.geometry("900x700")

## -- Create Plot object on GUI --
fig = Figure()
ax = fig.add_subplot(111)

ax.set_title("Serial Data")
ax.set_xlabel("Time")
ax.set_ylabel("Setpoint")
ax.set_xlim(0,100)
ax.set_ylim(0,360)
lines1 = ax.plot([],[])[0]
lines2 = ax.plot([],[])[0]

# ax2 = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().place(x=50,y=200,width=600,height=400)
canvas.draw()

## -- Create Button --
root.update()
start = tk.Button(root, text="Start", font=('Arial',12), command = lambda: plot_start())
start.place(x=100,y=630)

root.update()
stop = tk.Button(root, text="Stop", font=('Arial',12), command = lambda: plot_stop())
stop.place(x=start.winfo_x()+start.winfo_reqwidth()+40, y=630)

root.after(1,plot_data)
root.mainloop()