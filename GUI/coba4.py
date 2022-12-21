from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import tkinter as tk
import numpy as np
import serial as sr
import time
from PIL import Image,ImageTk

data1 = np.array([])
data2 = np.array([])
data3 = np.array([])
data4 = np.array([])
cond = False

# --- Start Serial ---
s = sr.Serial('COM5',9600, timeout=1)
time.sleep(2)
s.reset_input_buffer() 

# -- Plot Data --
def plot_data():
    global cond,data1,data2,data3,data4, stat
    if (cond==True and stat == 1):
        a = s.readline()
        string = a.decode()
        p = string.split(",")
        sp = float(p[0])
        pot = float(p[1])
        error = float(p[2])
        tacho = float(p[3])

        if(len(data1) < 100):
            data1 = np.append(data1,sp)
        else:
            data1[0:99] = data1[1:100]
            data1[99] = sp
        
        if(len(data2) < 100):
            data2 = np.append(data2,pot)
        else:
            data2[0:99] = data2[1:100]
            data2[99] = pot
        
        if(len(data3) < 100):
            data3 = np.append(data3,error)
        else:
            data3[0:99] = data3[1:100]
            data3[99] = error

        # data1 = np.append(data1, float(p[0]))
        # data2 = np.append(data2, float(p[1]))

        lines1.set_xdata(np.arange(0,len(data1)))
        lines1.set_ydata(data1)
        lines2.set_xdata(np.arange(0,len(data2)))
        lines2.set_ydata(data2)
        lines3.set_xdata(np.arange(0,len(data3)))
        lines3.set_ydata(data3)

        canvas1.draw()
        canvas3.draw()
    
    if(cond == True and stat == 2):
        a = s.readline()
        string = a.decode()
        p = string.split(",")
        sp = float(p[0])
        pot = float(p[1])
        error = float(p[2])
        tacho = float(p[3])

        if(len(data1) < 100):
            data1 = np.append(data1,sp)
        else:
            data1[0:99] = data1[1:100]
            data1[99] = sp
        
        if(len(data4) < 100):
            data4 = np.append(data4,tacho)
        else:
            data4[0:99] = data4[1:100]
            data4[99] = tacho
        
        if(len(data3) < 100):
            data3 = np.append(data3,error)
        else:
            data3[0:99] = data3[1:100]
            data3[99] = error

        lines1.set_xdata(np.arange(0,len(data1)))
        lines1.set_ydata(data1)
        lines4.set_xdata(np.arange(0,len(data4)))
        lines4.set_ydata(data2)
        lines3.set_xdata(np.arange(0,len(data3)))
        lines3.set_ydata(data3)

        canvas2.draw()
        canvas3.draw()
    root.after(1,plot_data)

def plot_start1():
    global cond, stat
    cond = True
    stat = 1
    s.reset_input_buffer()

def plot_start2():
    global cond, stat
    cond = True
    stat = 2
    s.reset_input_buffer()

def plot_stop1():
    global cond, stat
    cond = False
    stat = 1

def plot_stop2():
    global cond, stat
    cond = False
    stat = 2

root = tk.Tk()
root.title('Real Time Plot')
# root.geometry("1400x900")
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
# root.attributes('-fullscreen', 1)

## -- Create Plot object on GUI --
fig1 = Figure()
fig2 = Figure()
fig3 = Figure()

## Subplot Setpoint
ax = fig1.add_subplot(111, facecolor = "#E8F9FD")
ax.set_title("Position Controller Motor DC")
ax.grid()
# ax.legend()
# ax.set_xlabel("Time")
# ax.set_ylabel("Setpoint")
ax.set_xlim(0,100)
ax.set_ylim(0,360)
lines1 = ax.plot([],[])[0]
lines2 = ax.plot([],[])[0]

# Subplot Error
ax2 = fig2.add_subplot(111, facecolor = "#E8F9FD")
ax2.set_title("Speed Controller Motor DC")
ax2.grid()
# ax2.legend()
# ax.set_xlabel("Time")
# ax.set_ylabel("Setpoint")
ax2.set_xlim(0,100)
ax2.set_ylim(0,360)
lines1 = ax2.plot([],[])[0]
lines4 = ax2.plot([],[])[0]

ax3 = fig3.add_subplot(111, facecolor = "#E8F9FD")
ax3.set_title("Error")
ax3.grid()
# ax3.legend()
# ax2.set_xlabel("Time")
# ax2.set_ylabel("Value")
ax3.set_xlim(0,100)
ax3.set_ylim(-50,50)
lines3 = ax3.plot([],[])[0]

canvas = Canvas(root, background="#59CE8F")

judul = "Feedback Educational Servo ES151 (Remake)"
canvas.create_text(200, 45, anchor=W, font=("Helvetica",'40','bold'),text = judul, fill = "#FF1E00")

#Kotak Kelompok
canvas.create_rectangle(50,100,500,300, outline="#E8F9FD", fill= '#E8F9FD')
canvas.create_text(200, 130, anchor=W, font=("Helvetica",'20','bold'),text = "Kelompok 1", fill = "#FF1E00")
canvas.create_text(70, 170, anchor=W, font=("Helvetica",'15','bold'),text = "Priyova Muhammad Rafief", fill = "#FF1E00")
canvas.create_text(70, 200, anchor=W, font=("Helvetica",'15','bold'),text = "Bodhi Setiawan", fill = "#FF1E00")
canvas.create_text(70, 230, anchor=W, font=("Helvetica",'15','bold'),text = "Octsana Dhiyaa Warsana", fill = "#FF1E00")
canvas.create_text(70, 260, anchor=W, font=("Helvetica",'15','bold'),text = "Karunia Dini Fadillah", fill = "#FF1E00")

#Kotak PID
canvas.create_rectangle(1050,100,1490,300, outline="#E8F9FD", fill= '#E8F9FD')
canvas.create_text(1220, 130, anchor=W, font=("Helvetica",'20','bold'),text = "Data PID", fill = "#FF1E00")
canvas.create_text(1070, 180, anchor=W, font=("Helvetica",'15','bold'),text = "Kp :", fill = "#FF1E00")
canvas.create_text(1070, 220, anchor=W, font=("Helvetica",'15','bold'),text = "Ki :", fill = "#FF1E00")
canvas.create_text(1070, 260, anchor=W, font=("Helvetica",'15','bold'),text = "Kd :", fill = "#FF1E00")

img = Image.open("Logo.png")
img = img.resize((200,200), Image.ANTIALIAS)
logo= ImageTk.PhotoImage(img)
canvas.create_image(680,200,anchor=W,image=logo)

canvas.create_rectangle(50,330,220,400, outline="#E8F9FD", fill= '#E8F9FD')
canvas.create_rectangle(550,330,720,400, outline="#E8F9FD", fill= '#E8F9FD')
canvas.pack(fill=BOTH, expand=1)

canvas1 = FigureCanvasTkAgg(fig1, master=root)
canvas1.get_tk_widget().place(x=50,y=420,width=450,height=300)
canvas1.draw()

canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas2.get_tk_widget().place(x=550,y=420,width=450,height=300)
canvas2.draw()

canvas3 = FigureCanvasTkAgg(fig3, master=root)
canvas3.get_tk_widget().place(x=1050,y=420,width=450,height=300)
canvas3.draw()

root.update()
start1 = tk.Button(root, text="Start", font=('Arial',12), background = "#59CE8F", activebackground="#E8F9FD", 
                    foreground= "#000000", activeforeground= "#000000", command = lambda: plot_start1())
start1.place(x=70,y=350)

root.update()
stop1 = tk.Button(root, text="Stop", font=('Arial',12), background = "#FF1E00", activebackground="#E8F9FD", 
                    foreground= "#000000", activeforeground= "#000000", command = lambda: plot_stop1())
start1.place(x=70,y=350)
stop1.place(x=start1.winfo_x()+start1.winfo_reqwidth()+40, y=350)

root.update()
start2 = tk.Button(root, text="Start", font=('Arial',12), background = "#59CE8F", activebackground="#E8F9FD", 
                    foreground= "#000000", activeforeground= "#000000", command = lambda: plot_start2())
start2.place(x=570,y=350)

root.update()
stop2 = tk.Button(root, text="Stop", font=('Arial',12), background = "#FF1E00", activebackground="#E8F9FD", 
                    foreground= "#000000", activeforeground= "#000000", command = lambda: plot_stop2())
stop2.place(x=start2.winfo_x()+start2.winfo_reqwidth()+40, y=350)

root.after(1,plot_data)
root.mainloop()