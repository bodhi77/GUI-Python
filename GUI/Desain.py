from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import tkinter as tk
import numpy as np
import serial as sr
import time
from PIL import Image,ImageTk
from matplotlib import style
from time import strftime

style.use("dark_background")

fc1="#171F24"
bg1="#03DAC5"
bg2="#CF6679"
fg1="#FFFFFF"
fg2="#000000"
text1="#FFFFFF"
fill2="#171F24"

FontGede=("Gama-Sans", 16)
FontCilik=("Gama-Serif", 12)
FontCilikBgt=("Gama-Serif",9)

root = tk.Tk()
root.title('Real Time Plot')
# root.geometry("1920x1080")
# width= root.winfo_screenwidth()
# height= root.winfo_screenheight()
# root.geometry("%dx%d" % (width, height))
root.attributes('-fullscreen', 1)
root.bind('<Escape>', lambda _: root.destroy())

bg = PhotoImage(file = "GUI/bg2.png")

canvas = Canvas(root, width=1920, height=1080)

canvas.pack(fill = "both", expand = True)

canvas.create_image( 0, 0, image = bg, anchor = "nw")

fig1 = Figure()
fig2 = Figure()
fig3 = Figure()

## Subplot Setpoint
ax = fig1.add_subplot(111, facecolor=fc1)
ax.set_title("Position Data Plot")
ax.grid()
# ax.legend()
# ax.set_xlabel("Time")
# ax.set_ylabel("Setpoint")
ax.set_xlim(0,100)
ax.set_ylim(0,360)

ax2 = fig2.add_subplot(111, facecolor=fc1)
ax2.set_title("Speed Data Plot")
ax2.grid()
# ax2.legend()
# ax.set_xlabel("Time")
# ax.set_ylabel("Setpoint")
ax2.set_xlim(0,100)
ax2.set_ylim(0,360)

ax3 = fig3.add_subplot(111, facecolor=fc1)
ax3.set_title("Error")
ax3.grid()
# ax3.legend()
# ax2.set_xlabel("Time")
# ax2.set_ylabel("Value")
ax3.set_xlim(0,100)
ax3.set_ylim(-50,50)

judul = "Motor Control GUI"

canvas.pack()

canvas.create_text(720, 30, anchor=W, font=(FontGede),text = judul, fill = text1)

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
 
 



def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
    
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# #Kotak Kelompok
# canvas.create_rectangle(50,100,500,300, outline=fill2, fill= fill2)
my_rectangle = round_rectangle(830,100,1430,420, radius=20, outline=text1,fill=fill2, stipple='gray50')
canvas.create_text(850, 130, anchor=W, font=(FontGede),text = "Kelompok 1", fill = text1)
canvas.create_text(850, 170, anchor=W, font=(FontCilikBgt),text = "Priyova M. R.\t(20/457197/SV/17644)", fill = text1)
canvas.create_text(850, 200, anchor=W, font=(FontCilikBgt),text = "Bodhi S.\t\t(20/464239/SV/18558)", fill = text1)
canvas.create_text(850, 230, anchor=W, font=(FontCilikBgt),text = "Octsana D. W.\t(20/464253/SV/18572)", fill = text1)
canvas.create_text(850, 260, anchor=W, font=(FontCilikBgt),text = "Karunia D. F.\t(20/464248/SV/18567)", fill = text1)
canvas.create_text(850, 290, anchor=W, font=(FontCilikBgt),text = "Dosen Pembimbing:\t Fahmizal, S.T., M.Sc.", fill = text1)
# Styling the label widget so that clock
# will look more attractive
lbl = Label(canvas, font=("Gama-Sans",24, "bold"), background=bg2, foreground='white')
# Label(ws,image=giant,bg='grey').pack()
# lbl.place(x=880, y=260)
 
# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor=NE)
time()

#Kotak PID
# canvas.create_rectangle(1050,100,1490,300, outline=fill2, fill= fill2)
my_rectangle = round_rectangle(50,100,170,300, radius=20, outline=text1, fill=fill2, stipple='gray50')
canvas.create_text(75, 130, anchor=W, font=(FontGede),text = "PID Gain", fill = text1)
canvas.create_text(60, 180, anchor=W, font=(FontCilik),text = "Kp :", fill = text1)
canvas.create_text(60, 220, anchor=W, font=(FontCilik),text = "Ki :", fill = text1)
canvas.create_text(60, 260, anchor=W, font=(FontCilik),text = "Kd :", fill = text1)

img = Image.open("GUI\Logo3.png")
img = img.resize((200,47), Image.ANTIALIAS)
logo= ImageTk.PhotoImage(img)
canvas.create_image(50,45,anchor=W,image=logo)

# canvas.create_rectangle(50,330,220,400, outline=fill2, fill= fill2)
# canvas.create_rectangle(550,330,720,400, outline=fill2, fill= fill2)
# canvas.pack(fill=BOTH, expand=1)

canvas1 = FigureCanvasTkAgg(fig1, master=root)
canvas1.get_tk_widget().place(x=180,y=100,width=600,height=320)
canvas1.draw()

canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas2.get_tk_widget().place(x=180,y=430,width=600,height=320)
canvas2.draw()

canvas3 = FigureCanvasTkAgg(fig3, master=root)
canvas3.get_tk_widget().place(x=830,y=430,width=600,height=320)
canvas3.draw()

root.update()
start1 = tk.Button(root, text="Start", font=(FontCilik), background = bg1, activebackground=fill2, foreground= fg1, activeforeground= fg2, width=10)
start1.place(x=100,y=340)

root.update()
stop1 = tk.Button(root, text="Stop", font=(FontCilik), background = bg2, activebackground=fill2, foreground= fg1, activeforeground= fg2, width=10)
start1.place(x=100,y=340)
stop1.place(x=100, y=start1.winfo_y()+start1.winfo_reqheight()+10)

root.update()
start2 = tk.Button(root, text="Start", font=(FontCilik), background = bg1, activebackground=fill2, foreground= fg1, activeforeground= fg2, width=10)
start2.place(x=100,y=670)

root.update()
stop2 = tk.Button(root, text="Stop", font=(FontCilik), background = bg2, activebackground=fill2, foreground= fg1, activeforeground= fg2,width=10)
stop2.place(x=100, y=start2.winfo_y()+start2.winfo_reqheight()+10)

# root.after(1,plot_data)
root.mainloop()