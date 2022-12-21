import serial 
import tkinter

arduino = serial.Serial('com4', 9600)

def len_on():
    arduino.write('1')

def len_off():
    arduino.write('0')

tk = tkinter.Tk

button = tkinter.Button

btn_on = button(tk, text ="ON", command = len_on)
btn_off = button(tk, text ="OFF", command = len_off)

btn_on.grid(row=0, column = 1)

tk.mainloop()



