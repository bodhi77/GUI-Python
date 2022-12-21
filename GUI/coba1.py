from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import serial as sr
import time

data = np.array([])
cond = False

# -- Plot Data --
def plot_data():
    global cond,data
    if (cond==True):
        a = s.readline()
        a.decode()
        if(len(data) < 100):
            data = np.append(data,float(a[0:4]))
        else:
            data[0:99] = data[1:100]
            data[99] = float(a[0:4])

        lines.set_xdata(np.arange(0,len(data)))
        lines.set_ydata(data)
        print(data)

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
lines = ax.plot([],[])[0]

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

# --- Start Serial ---
s = sr.Serial('COM5',9600, timeout=1)
time.sleep(2)
s.reset_input_buffer()

root.after(1,plot_data)
root.mainloop()