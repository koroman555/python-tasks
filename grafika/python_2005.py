# Намалювати діагональні лінії
max_w = 800
max_h = 600

from tkinter import Canvas
from tkinter import Tk
from time import sleep
import random

tk = Tk()

# -----------------------------------------------------------------------
# функція для малювання кола через
# координати центру + радіус
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle
# -----------------------------------------------------------------------

canvas = Canvas(tk, width = max_w, height = max_h)
canvas.pack()

input()
radius = 10
y = max_h

for x in range( 0, max_w//2, 30):
  canvas.create_circle( x, y, radius )
  y = y - 20
  radius = radius + 10
  canvas.update()
  sleep(0.5)

for x in range( max_w//2, max_w, 30):
  canvas.create_circle( x, y, radius )
  y = y + 20
  radius = radius - 10
  canvas.update()
  sleep(0.5)

tk.mainloop()