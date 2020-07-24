# Намалювати діагональні лінії
max_w = 800
max_h = 600

from tkinter import Canvas
from tkinter import Tk
from time import sleep
import random

tk = Tk()

# -----------------------------------------------------------------------
# функція для малюівння кола через
# координати цетру + радіус
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle
# -----------------------------------------------------------------------


all_colors = [
    'red','green','blue',
    'orange','yellow','pink',
    'purple','violet','magenta',
    'cyan'
]

canvas = Canvas(tk, width = max_w, height = max_h)
canvas.pack()

radius = 150

color = random.choice(all_colors)

canvas.create_circle(
    max_w/2, 
    max_h/2, 
    radius,
    fill = color
)

tk.mainloop()