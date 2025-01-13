from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.title = "ritprogram"

canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

last_x, last_y = None, None


def start_drawing(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y


def draw(event):
    global last_x, last_y
    if last_x and last_y:
        canvas.create_line(last_x, last_y, event.x,
                           event.y, fill="black", width=2)
        last_x, last_y = event.x, event.y


def reset(event):
    global last_x, last_y
    last_x, last_y = None, None


canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset)

root.mainloop()
