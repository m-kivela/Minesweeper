# Simply a file for testing purposes. Not necessary for running the program.
"""
from game import *
from debug_interface import terminal_interface

game = Game(5,5,5,1)

def run() -> None:
    terminal_interface(game)

    x = int(input("Input X-coord: "))
    y = int(input("Input Y-coord: "))

    square = game.object_at(x,y)
    game.play_turn(square)
    print(f"Turn number: {game._turn}")
    print(f"Game won: {game._gamewon}")
    print(f"Game lost: {game._gamelost}")
"""
from tkinter import font
from tkinter import *
from tkinter import ttk

def savePosn(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    canvas.create_line((lastx, lasty, event.x, event.y))
    savePosn(event)

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", savePosn)
canvas.bind("<B1-Motion>", addLine)

customfont = font.Font(family="Helvetica", size=20, weight="bold")
canvas.create_text(100, 100, anchor="center", text="5", fill="red")
canvas.create_text(100, 100, anchor="nw", text="5", fill="blue")

root.mainloop()