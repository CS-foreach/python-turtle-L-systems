from turtle import *
from tkinter import ALL

def centerScreenCanvasCoords(x=0, y=0):
    screenWidth = screensize()[0]
    screenHeight = screensize()[1]

    x = (x + (screenWidth - window_width())/2)/screenWidth
    y = (y + (screenHeight + window_height())/2)/screenHeight

    return (x, y)

def doZoom(factor):
    x, y = centerScreenCanvasCoords()
    x = getcanvas().canvasx(x)
    y = getcanvas().canvasy(y)
    getcanvas().scale(ALL, x, y, factor, factor)

def zoomIn():
    doZoom(1.15)

def zoomOut():
    doZoom(.85)

def panLeft():
    getcanvas().xview_scroll(-1, "units")

def panRight():
    getcanvas().xview_scroll(1, "units")

def panUp():
    getcanvas().yview_scroll(-1, "units")

def panDown():
    getcanvas().yview_scroll(1, "units")

def setListens():
    onkeypress(bye, "q")
    onkeypress(panUp, "w")
    onkeypress(panLeft, "a")
    onkeypress(panDown, "s")
    onkeypress(panRight, "d")
    onkeypress(zoomIn, "Up")
    onkeypress(zoomOut, "Down")

def initialize():
    setListens()
    listen()
    mainloop()
