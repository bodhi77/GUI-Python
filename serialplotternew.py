import serial
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as Tk
from tkinter.ttk import Frame

class Window(Frame):
    def __init__(self, figure, master, SerialReference):
        Frame.__init__(self, master)
        self.entries = []
        self.setPoint = None
        self.master = master        # a reference to the master window
        self.serialReference = SerialReference      # keep a reference to our serial connection so that we can use it for bi-directional communicate from this class
        self.initWindow(figure)     # initialize the window with our settings

    def initWindow(self, figure):
        self.master.title("Real Time Plot")
        canvas = FigureCanvasTkAgg(figure, master=self.master)
        toolbar = NavigationToolbar2Tk(canvas, self.master)
        canvas.get_tk_widget().pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

def main():
    s = serial.Serial('/dev/ttyACM0',115200)   # initializes all required variables
    s.readSerialStart() # starts background thread

    # plotting starts below
    fig = plt.figure()

    # put our plot onto Tkinter's GUI
    root = Tk.Tk()
    app = Window(fig, root, s)

    for i in range(100):
        lines.append(ax.plot([], [])
    anim = animation.FuncAnimation(fig, s.getSerialData)

    root.mainloop()   # use this instead of plt.show() since we are encapsulating everything in Tkinter
    s.close()