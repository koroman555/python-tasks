# Намалювати діагональні лінії


from tkinter import Canvas
from tkinter import Tk
from time import sleep
import random

tk = Tk()

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

Canvas.create_circle = _create_circle

colors = [
    'red','green','blue',
    'orange','yellow','pink',
    'purple','violet','magenta',
    'cyan'
]

max_w = 800
max_h = 600

canvas = Canvas(tk, width = max_w, height = max_h)
canvas.pack()

interval = 30
for r in range( max_h//2, 10, interval * -1 ):
    color = random.choice(colors)
    canvas.create_circle(
      max_w/2, 
      max_h/2, 
      r,
      fill = color
    )
    canvas.update()
    sleep(1)

tk.mainloop()