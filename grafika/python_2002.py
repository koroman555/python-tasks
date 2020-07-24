# Намалювати діагональні лінії
max_w = 800
max_h = 600

from tkinter import Canvas
from tkinter import Tk
from time import sleep
tk = Tk()

canvas = Canvas(tk, width = max_w, height = max_h)
canvas.pack()

input()
interval = 20
for x in range(0, max_w+interval, interval):
  canvas.create_line(x, 0, max_w - x, max_h)
  canvas.update()
  sleep(0.1)

tk.mainloop()