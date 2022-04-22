from turtle import *
from tkinter import ALL, EventType

lSystems = {
    "plant": ("f", "f[+f]f[-f]f", 26, 5, "bottom"),
    "quadKochSq":("f+f+f+f", "f-f+f+ff-f-f+f", 90, 3, "center"),
    "KochFlake":("f++f++f", "f-f++f-f", 60, 20, "center")
}

debug = False
structure = "plant"
route = ""

axiom, rewriteRule, phi, distance, windowAlign = lSystems[structure]
positionStack = []

def f():
    forward(distance)

def cw():
    right(phi)

def ccw():
    left(phi)

def doZoom(event):
    x = getcanvas().canvasx(event.x)
    y = getcanvas().canvasy(event.y)
    factor = 1.001 ** event.delta
    getcanvas().scale(ALL, x, y, factor, factor)

def scrollTo(x, y):
    x += ((screensize()[0] - window_width())//2)
    y += ((screensize()[1] + window_height())//2)

    x /= screensize()[0]
    y /= screensize()[1]

    if debug: print(f"Centering on: ({x}, {y})")

    getcanvas().xview_moveto(x)
    getcanvas().yview_moveto(1-y)

def tPush():
    top = (pos()[0], pos()[1], heading())
    if (debug): print("Push of {top}.")
    positionStack.append(top)

def tPop():
    top = positionStack.pop()
    if (debug): print(f"Pop to {top}.")
    goto(top[0], top[1])
    setheading(top[2])

def initialize():
    setup(.3,.3)
    screensize(2000,2000)
    ht()
    tracer(9)
    #bgcolor("blue")

    left(90)
    pensize(2)
    up()
    sety({"bottom":(-970), "center":(0)}[windowAlign])
    down()
    onkeypress(bye, "q")
    onkeypress(reset, "r")
    onkeypress(runRules, "d")
    onscreenclick(scrollTo)
    getcanvas().bind("<MouseWheel>", doZoom)
    listen()

def rewrite(parent):
    child = ""
    for _ in parent:
        if (_ == "f"):
            child += rewriteRule
        else:
            child += _
    return child

RULES = {
    "f":f,
    "-":cw,
    "+":ccw,
    "[":tPush,
    "]":tPop
}

def generateIteration(generations, axiom):
    newRoute = axiom
    for i in range(generations):
        newRoute = rewrite(newRoute)
    return newRoute

def runRules():
    global route
    if (debug): print(f"Running structure: {route}")
    for _ in route:
        RULES[_]()

def main() -> None:
    global route
    generations = 5
    initialize()
    route = generateIteration(generations, axiom)

if __name__ == "__main__":
    main()
    mainloop()
