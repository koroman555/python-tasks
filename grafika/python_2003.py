# Намалювати шахматну дошку
# Використати вхідні параметри:
klitynka = 50
start_x=200
start_y=100

from tkinter import Canvas
from tkinter import Tk
from time import sleep
tk = Tk()

max_w = 800
max_h = 600
canvas = Canvas(tk, width = max_w, height = max_h)
canvas.pack()

# Рамка
canvas.create_rectangle(start_x, start_y, start_x + klitynka * 8, start_y + klitynka * 8)

# Чорні 1
for y in range(start_y, start_y + klitynka * 8, klitynka * 2):
    for x in range(start_x, start_x + klitynka * 8, klitynka * 2):
        canvas.create_rectangle(x,y, x + klitynka, y + klitynka, fill = 'black')
        canvas.update()
        sleep(0.1)

# Чорні 2
for y in range(start_y + klitynka, start_y + klitynka * 8, klitynka * 2):
    for x in range(start_x + klitynka, start_x + klitynka * 8, klitynka * 2):
        canvas.create_rectangle(x,y, x + klitynka, y + klitynka, fill = 'black')
        canvas.update()
        sleep(0.1)




tk.mainloop()